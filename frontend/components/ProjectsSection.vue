<template>
  <section id="projects" class="py-20 md:py-32">
    <div class="container mx-auto px-6">
      <!-- Section header -->
      <div class="text-center mb-16">
        <h2 ref="sectionTitle" class="section-title">
          Featured Projects
        </h2>
        <p class="text-text-secondary text-lg max-w-2xl mx-auto">
          A selection of my recent work and side projects
        </p>
      </div>
      
      <!-- Projects grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <ProjectCard 
          v-for="project in projects" 
          :key="project.id"
          :project="project"
          class="project-card"
        />
      </div>
      
      <!-- View all link -->
      <div class="text-center mt-12">
        <NuxtLink to="/projects" class="inline-flex items-center text-accent hover:text-accent/80 transition-colors">
          View All Projects
          <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </NuxtLink>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { onMounted, onUnmounted, computed, ref } from 'vue'

// Template refs
const sectionTitle = ref(null)

// Fetch featured projects
const { data: projectsData } = await useAsyncData('featured-projects', () => useApi().getProjects(true))
const projects = computed(() => projectsData.value?.projects || [])

// Store animation instances for cleanup
let titleAnimation = null
let cardsAnimation = null

onMounted(() => {
  // Register ScrollTrigger plugin
  gsap.registerPlugin(ScrollTrigger)
  
  // Animate section title using ref
  if (sectionTitle.value) {
    titleAnimation = gsap.from(sectionTitle.value, {
      scrollTrigger: {
        trigger: sectionTitle.value,
        start: 'top 80%',
        id: 'projects-title'
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
  
  // Animate project cards with scoped selector
  const cards = document.querySelectorAll('#projects .project-card')
  if (cards.length > 0) {
    cardsAnimation = gsap.from(cards, {
      scrollTrigger: {
        trigger: cards[0],
        start: 'top 80%',
        id: 'projects-cards'
      },
      y: 50,
      opacity: 0,
      duration: 0.8,
      stagger: 0.2,
      onComplete: () => {
        // Ensure all cards are visible
        gsap.set(cards, { clearProps: 'all' })
      }
    })
  }
})

onUnmounted(() => {
  // Clean up ScrollTrigger instances
  if (titleAnimation) {
    titleAnimation.scrollTrigger?.kill()
    titleAnimation.kill()
  }
  if (cardsAnimation) {
    cardsAnimation.scrollTrigger?.kill()
    cardsAnimation.kill()
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
  /* Fallback for webkit rendering issues */
  color: transparent;
  /* Force repaint */
  will-change: transform;
}

.project-card {
  opacity: 1 !important;
}
</style>