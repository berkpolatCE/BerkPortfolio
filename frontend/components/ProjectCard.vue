<template>
  <article 
    ref="cardRef"
    class="group relative bg-secondary rounded-xl overflow-hidden border border-border hover:border-accent/50 transition-all duration-500 cursor-pointer"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
    @click="navigateToProject"
  >
    <!-- Project image -->
    <div class="aspect-video overflow-hidden bg-primary/50 border border-border/50 rounded-t-xl">
      <img 
        v-if="project.image" 
        :src="project.image" 
        :alt="project.title"
        class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
      />
      <div v-else class="w-full h-full flex items-center justify-center">
        <span class="text-text-secondary text-6xl font-display opacity-20">{{ project.title?.[0] || '?' }}</span>
      </div>
    </div>
    
    <!-- Content -->
    <div class="p-6">
      <!-- Technologies -->
      <div class="flex flex-wrap gap-2 mb-4">
        <span 
          v-for="tech in project.technologies?.slice(0, 3)" 
          :key="tech"
          :class="getTechTagClass(tech)"
          class="text-xs px-3 py-1.5 rounded-full font-medium transition-all duration-300 hover:scale-105"
        >
          {{ tech }}
        </span>
      </div>
      
      <!-- Title -->
      <h3 class="text-xl font-semibold mb-2 group-hover:text-accent transition-colors">
        {{ project.title }}
      </h3>
      
      <!-- Description -->
      <p class="text-text-secondary line-clamp-3">
        {{ project.description }}
      </p>
    </div>
    
    <!-- Hover effect overlay -->
    <div class="absolute inset-0 bg-gradient-to-t from-accent/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
  </article>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { gsap } from 'gsap'

interface Project {
  id: number
  title: string
  description: string
  image?: string
  technologies?: string[]
  github_url?: string
  live_url?: string
  featured?: boolean
}

const props = defineProps<{
  project: Project
}>()

const router = useRouter()
const cardRef = ref(null)

const handleMouseEnter = (e: MouseEvent) => {
  if (!cardRef.value) return
  
  gsap.to(cardRef.value, {
    y: -5,
    duration: 0.3,
    ease: 'power2.out'
  })
}

const handleMouseLeave = () => {
  if (!cardRef.value) return
  
  gsap.to(cardRef.value, {
    y: 0,
    duration: 0.3,
    ease: 'power2.out'
  })
}

const navigateToProject = () => {
  router.push(`/projects/${props.project.id}`)
}

const getTechTagClass = (tech: string): string => {
  const techLower = tech.toLowerCase()
  
  // Define tech-specific colors that work with the dark theme
  const techColors: Record<string, string> = {
    // Languages
    'python': 'bg-blue-500/20 text-blue-300 border border-blue-500/30',
    'javascript': 'bg-yellow-500/20 text-yellow-300 border border-yellow-500/30',
    'typescript': 'bg-blue-600/20 text-blue-300 border border-blue-600/30',
    'c++': 'bg-purple-500/20 text-purple-300 border border-purple-500/30',
    'java': 'bg-orange-500/20 text-orange-300 border border-orange-500/30',
    'c#': 'bg-green-600/20 text-green-300 border border-green-600/30',
    'go': 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30',
    'rust': 'bg-orange-600/20 text-orange-300 border border-orange-600/30',
    'php': 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/30',
    'ruby': 'bg-red-500/20 text-red-300 border border-red-500/30',
    'swift': 'bg-orange-500/20 text-orange-300 border border-orange-500/30',
    
    // Frameworks & Libraries
    'react': 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30',
    'vue': 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30',
    'angular': 'bg-red-600/20 text-red-300 border border-red-600/30',
    'django': 'bg-green-700/20 text-green-300 border border-green-700/30',
    'flask': 'bg-gray-600/20 text-gray-300 border border-gray-600/30',
    'node.js': 'bg-green-600/20 text-green-300 border border-green-600/30',
    'express': 'bg-gray-500/20 text-gray-300 border border-gray-500/30',
    'fastapi': 'bg-teal-500/20 text-teal-300 border border-teal-500/30',
    'next.js': 'bg-gray-800/40 text-gray-200 border border-gray-700/50',
    'nuxt': 'bg-green-500/20 text-green-300 border border-green-500/30',
    
    // Tools & Technologies
    'docker': 'bg-blue-600/20 text-blue-300 border border-blue-600/30',
    'kubernetes': 'bg-blue-700/20 text-blue-300 border border-blue-700/30',
    'aws': 'bg-orange-600/20 text-orange-300 border border-orange-600/30',
    'git': 'bg-red-600/20 text-red-300 border border-red-600/30',
    'postgresql': 'bg-blue-700/20 text-blue-300 border border-blue-700/30',
    'mongodb': 'bg-green-600/20 text-green-300 border border-green-600/30',
    'redis': 'bg-red-600/20 text-red-300 border border-red-600/30',
    'mysql': 'bg-blue-600/20 text-blue-300 border border-blue-600/30',
    'tensorflow': 'bg-orange-500/20 text-orange-300 border border-orange-500/30',
    'pytorch': 'bg-red-500/20 text-red-300 border border-red-500/30',
    
    // Default fallback
    'default': 'bg-accent/20 text-accent border border-accent/30'
  }
  
  // Check for exact match or partial match
  for (const [key, value] of Object.entries(techColors)) {
    if (techLower === key || techLower.includes(key)) {
      return value
    }
  }
  
  // Return default if no match found
  return techColors.default
}
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>