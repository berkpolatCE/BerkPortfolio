<template>
  <article 
    ref="cardRef"
    class="group relative bg-secondary rounded-xl overflow-hidden border border-border hover:border-accent/50 transition-all duration-500 cursor-pointer"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
    @click="navigateToProject"
  >
    <!-- Project image -->
    <div class="aspect-video overflow-hidden bg-primary/50">
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
          class="text-xs px-3 py-1 bg-primary rounded-full text-text-secondary"
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
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>