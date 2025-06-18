<template>
  <section id="skills" class="py-20 md:py-32 bg-secondary/30">
    <div class="container mx-auto px-6">
      <!-- Section header -->
      <div class="text-center mb-16">
        <h2 ref="sectionTitle" class="section-title">
          Skills & Expertise
        </h2>
        <p class="text-text-secondary text-lg max-w-2xl mx-auto">
          Technologies and Tools
        </p>
      </div>
      
      <!-- Categories Grid -->
      <div class="max-w-6xl mx-auto">
        <!-- Category Cards -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          <SkillCategoryCard
            v-for="category in skillCategories"
            :key="category.id"
            :category="category"
            :is-expanded="expandedCategory === category.id"
            @click="toggleCategory(category.id)"
          />
        </div>
        
        <!-- Expanded Skills Tree -->
        <Transition
          name="skills-tree"
          @enter="onEnter"
          @leave="onLeave"
        >
          <div v-if="expandedCategory" class="skills-tree-container relative">
            <!-- Connection Lines SVG -->
            <svg class="absolute inset-0 w-full h-full pointer-events-none" style="z-index: 1;">
              <defs>
                <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" :stop-color="getCategoryColor(expandedCategory)" stop-opacity="0.8" />
                  <stop offset="100%" :stop-color="getCategoryColor(expandedCategory)" stop-opacity="0.4" />
                </linearGradient>
              </defs>
              <g ref="linesGroup"></g>
            </svg>
            
            <!-- Skills Grid -->
            <div 
              ref="skillsGrid"
              class="skills-grid relative z-10"
              :class="`grid-${expandedCategory}`"
            >
              <TransitionGroup
                name="skill-item"
                @enter="onSkillEnter"
                @leave="onSkillLeave"
              >
                <div
                  v-for="(skill, index) in currentCategorySkills"
                  :key="`${expandedCategory}-${skill.name}`"
                  :data-index="index"
                  class="skill-node"
                >
                  <SkillCard :skill="skill" />
                </div>
              </TransitionGroup>
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, nextTick, watch } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import SkillCategoryCard from './SkillCategoryCard.vue'

// Template refs
const sectionTitle = ref<HTMLElement | null>(null)
const skillsGrid = ref<HTMLElement | null>(null)
const linesGroup = ref<SVGGElement | null>(null)

const expandedCategory = ref<string | null>(null)

// Store animation instance for cleanup
let titleAnimation: gsap.core.Tween | null = null
let linesTimeline: gsap.core.Timeline | null = null

// Fetch skills data
const { data: skillsData } = await useAsyncData('skills', () => useApi().getSkills())

// Define skill interface
interface Skill {
  name: string
  level: string
}

// Define cybersecurity tool names
const cybersecurityTools = ['Nmap', 'Metasploit', 'SQLMap', 'Burp Suite']
const generalTools = ['Git', 'Linux', 'Windows']

// Organize skills into categories
const skillCategories = computed(() => {
  if (!skillsData.value) return []
  
  const technical = skillsData.value.technical
  const soft = skillsData.value.soft || []
  
  // Separate tools into cybersecurity and general
  const allTools: Skill[] = technical?.tools || []
  const cyberTools = allTools.filter((tool: Skill) => cybersecurityTools.includes(tool.name))
  const genTools = allTools.filter((tool: Skill) => generalTools.includes(tool.name))
  
  return [
    {
      id: 'programming',
      name: 'Programming',
      skills: technical?.languages || []
    },
    {
      id: 'frameworks',
      name: 'Frameworks',
      skills: [
        ...(technical?.frontend || []),
        ...(technical?.backend || [])
      ]
    },
    {
      id: 'cybersecurity',
      name: 'Cybersecurity',
      skills: [
        ...(technical?.cybersecurity || []),
        ...cyberTools
      ]
    },
    {
      id: 'general',
      name: 'General',
      skills: [
        ...genTools,
        ...soft.map((skill: string) => ({ name: skill, level: '90%' }))
      ]
    }
  ]
})

const currentCategorySkills = computed(() => {
  if (!expandedCategory.value) return []
  const category = skillCategories.value.find(c => c.id === expandedCategory.value)
  return category?.skills || []
})

// Get category color
const getCategoryColor = (categoryId: string) => {
  const colors = {
    programming: '#3b82f6',
    frameworks: '#10b981',
    cybersecurity: '#ef4444',
    general: '#8b5cf6'
  }
  return colors[categoryId] || '#00ffaa'
}

// Animation state tracking
const isAnimating = ref(false)
const pendingCategory = ref<string | null>(null)

// Toggle category expansion
const toggleCategory = (categoryId: string) => {
  // Prevent clicks during animation
  if (isAnimating.value) return
  
  if (expandedCategory.value === categoryId) {
    // Closing current category
    isAnimating.value = true
    expandedCategory.value = null
    setTimeout(() => {
      isAnimating.value = false
    }, 600)
  } else {
    // Opening or switching category
    isAnimating.value = true
    
    if (expandedCategory.value) {
      // Smooth transition between categories
      isSwitchingCategories = true
      
      // First, fade out the lines
      if (linesGroup.value) {
        const lines = linesGroup.value.querySelectorAll('path')
        if (lines.length > 0) {
          gsap.to(lines, {
            opacity: 0,
            duration: 0.2,
            ease: 'power2.in'
          })
        }
      }
      
      // Then switch categories with a slight delay
      setTimeout(() => {
        expandedCategory.value = categoryId
        setTimeout(() => {
          isAnimating.value = false
          isSwitchingCategories = false
        }, 600)
      }, 150)
    } else {
      // No category open, just expand
      isSwitchingCategories = false
      expandedCategory.value = categoryId
      setTimeout(() => {
        isAnimating.value = false
      }, 600)
    }
  }
}

// Track if lines are currently being drawn
let isDrawingLines = false

// Draw connection lines
const drawConnectionLines = async () => {
  if (isDrawingLines) return // Prevent multiple simultaneous draws
  
  await nextTick()
  
  if (!linesGroup.value || !skillsGrid.value || !expandedCategory.value) return
  
  isDrawingLines = true
  
  // Kill any existing timeline
  if (linesTimeline) {
    linesTimeline.kill()
    linesTimeline = null
  }
  
  // Clear existing lines with fade out if they exist
  const existingLines = linesGroup.value.querySelectorAll('path')
  if (existingLines.length > 0) {
    await gsap.to(existingLines, {
      opacity: 0,
      duration: 0.2,
      ease: 'power2.in',
      onComplete: () => {
        while (linesGroup.value?.firstChild) {
          linesGroup.value.removeChild(linesGroup.value.firstChild)
        }
      }
    })
  }
  
  // Small delay to ensure skills are positioned
  await new Promise(resolve => setTimeout(resolve, 50))
  
  const categoryCard = document.querySelector(`.skill-category-card.is-expanded`)
  if (!categoryCard || !linesGroup.value) return
  
  const categoryRect = categoryCard.getBoundingClientRect()
  const containerRect = skillsGrid.value.getBoundingClientRect()
  
  const skills = skillsGrid.value.querySelectorAll('.skill-node')
  if (skills.length === 0) return
  
  const paths: SVGPathElement[] = []
  
  skills.forEach((skill, idx) => {
    const skillRect = skill.getBoundingClientRect()
    
    // Calculate positions relative to the SVG container
    const startX = categoryRect.left + categoryRect.width / 2 - containerRect.left
    const startY = 0
    const endX = skillRect.left + skillRect.width / 2 - containerRect.left
    const endY = skillRect.top - containerRect.top + 20
    
    // Create more organic curved paths
    const midY = startY + (endY - startY) * 0.6
    const controlX = startX + (endX - startX) * 0.3
    
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path') as SVGPathElement
    path.setAttribute('d', `M ${startX} ${startY} Q ${controlX} ${midY} ${endX} ${endY}`)
    path.setAttribute('stroke', 'url(#lineGradient)')
    path.setAttribute('stroke-width', '3')
    path.setAttribute('fill', 'none')
    path.setAttribute('opacity', '0.9') // Start with final opacity
    
    linesGroup.value!.appendChild(path)
    paths.push(path)
  })
  
  // Animate lines with stagger
  linesTimeline = gsap.timeline({
    onComplete: () => {
      isDrawingLines = false
    }
  })
  
  paths.forEach((path, index) => {
    const length = path.getTotalLength()
    path.style.strokeDasharray = length.toString()
    path.style.strokeDashoffset = length.toString()
    
    // Only animate the stroke, not opacity
    linesTimeline!.to(path, {
      strokeDashoffset: 0,
      duration: 0.6,
      ease: 'power2.out'
    }, index * 0.03)
  })
}

// Track if we're switching between categories
let isSwitchingCategories = false

// Animation handlers
const onEnter = (el: Element) => {
  gsap.set(el, { 
    opacity: 0, 
    height: 0,
    overflow: 'hidden'
  })
  gsap.to(el, {
    opacity: 1,
    height: 'auto',
    duration: 0.4,
    ease: 'power3.out',
    onComplete: () => {
      gsap.set(el, { overflow: 'visible' })
      // Only draw lines on initial open, not when switching
      if (!isSwitchingCategories) {
        drawConnectionLines()
      }
    }
  })
}

const onLeave = (el: Element) => {
  // Fade out lines smoothly first
  if (linesGroup.value) {
    const lines = linesGroup.value.querySelectorAll('path')
    if (lines.length > 0) {
      gsap.to(lines, {
        opacity: 0,
        duration: 0.2,
        ease: 'power2.in',
        stagger: 0.01,
        onComplete: () => {
          // Kill timeline after fade
          if (linesTimeline) {
            linesTimeline.kill()
            linesTimeline = null
          }
          // Clear lines
          while (linesGroup.value?.firstChild) {
            linesGroup.value.removeChild(linesGroup.value.firstChild)
          }
        }
      })
    }
  }
  
  gsap.set(el, { overflow: 'hidden' })
  gsap.to(el, {
    opacity: 0,
    height: 0,
    duration: 0.3,
    ease: 'power3.in'
  })
}

const onSkillEnter = (el: Element) => {
  const index = parseInt(el.getAttribute('data-index') || '0')
  gsap.fromTo(el, 
    {
      opacity: 0,
      y: 15,
      scale: 0.95
    },
    {
      opacity: 1,
      y: 0,
      scale: 1,
      duration: 0.3,
      delay: index * 0.02,
      ease: 'power2.out'
    }
  )
}

const onSkillLeave = (el: Element) => {
  gsap.to(el, {
    opacity: 0,
    y: -10,
    scale: 0.95,
    duration: 0.15,
    ease: 'power2.in'
  })
}

// Watch for window resize to redraw lines
let resizeTimer: number | null = null
const handleResize = () => {
  if (resizeTimer) clearTimeout(resizeTimer)
  resizeTimer = window.setTimeout(() => {
    if (expandedCategory.value) {
      drawConnectionLines()
    }
  }, 250)
}

onMounted(() => {
  // Register ScrollTrigger plugin
  gsap.registerPlugin(ScrollTrigger)
  
  // Animate section title using ref
  if (sectionTitle.value) {
    titleAnimation = gsap.from(sectionTitle.value, {
      scrollTrigger: {
        trigger: sectionTitle.value,
        start: 'top 80%',
        id: 'skills-title'
      },
      y: 30,
      opacity: 0,
      duration: 1,
      onComplete: () => {
        // Ensure final state is applied
        gsap.set(sectionTitle.value, { clearProps: 'all' })
      }
    })
  }
  
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  // Clean up ScrollTrigger instance
  if (titleAnimation) {
    titleAnimation.scrollTrigger?.kill()
    titleAnimation.kill()
  }
  
  if (linesTimeline) {
    linesTimeline.kill()
  }
  
  window.removeEventListener('resize', handleResize)
})

// Watch for category changes but only draw lines if container is already visible
watch(expandedCategory, async (newVal, oldVal) => {
  if (newVal && oldVal) {
    // Switching between categories - wait for skills to be positioned
    await nextTick()
    setTimeout(() => {
      if (expandedCategory.value === newVal) { // Ensure we're still on the same category
        drawConnectionLines()
      }
    }, 100)
  }
})
</script>

<style scoped>
.section-title {
  @apply font-display text-4xl md:text-5xl font-bold mb-4 text-white;
  position: relative;
  background: linear-gradient(to right, #ffffff 0%, #a3a3a3 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
  will-change: transform;
}

.skills-tree-container {
  @apply relative min-h-[300px];
}

.skills-grid {
  @apply grid gap-4 pt-20;
}

.grid-programming {
  @apply grid-cols-2 md:grid-cols-4;
}

.grid-frameworks {
  @apply grid-cols-2 md:grid-cols-3 lg:grid-cols-5;
}

.grid-cybersecurity {
  @apply grid-cols-1 md:grid-cols-3;
}

.grid-general {
  @apply grid-cols-2 md:grid-cols-4;
}

.skill-node {
  @apply relative;
}

/* Transitions */
.skills-tree-enter-active {
  transition: opacity 0.4s ease-out;
}

.skills-tree-leave-active {
  transition: opacity 0.2s ease-in;
}

.skills-tree-enter-from {
  opacity: 0;
}

.skills-tree-leave-to {
  opacity: 0;
}

/* Disable Vue's default transitions for skill items since we're using GSAP */
.skill-item-enter-active,
.skill-item-leave-active,
.skill-item-move {
  transition: none !important;
}

/* Skills container styling */
.skill-node {
  will-change: transform, opacity;
}
</style>