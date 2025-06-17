<template>
  <div 
    ref="cardRef"
    class="group relative bg-primary border border-border rounded-lg p-4 hover:border-accent/50 transition-all duration-300 cursor-pointer"
    @mouseenter="handleHover"
    @mouseleave="handleLeave"
  >
    <!-- Skill content -->
    <div class="flex flex-col items-center text-center">
      <!-- Icon or first letter -->
      <div class="w-12 h-12 bg-secondary rounded-lg flex items-center justify-center mb-3 group-hover:bg-accent/20 transition-colors duration-300">
        <span class="text-xl font-display text-text-secondary group-hover:text-accent transition-colors duration-300">
          {{ skill.name[0] }}
        </span>
      </div>
      
      <!-- Skill name -->
      <h4 class="font-medium text-sm mb-2">{{ skill.name }}</h4>
      
      <!-- Proficiency indicator -->
      <div class="w-full bg-secondary rounded-full h-1.5 overflow-hidden">
        <div 
          ref="progressRef"
          class="h-full bg-gradient-to-r from-accent to-accent/60 rounded-full transform origin-left scale-x-0"
          :style="{ width: skill.level }"
        ></div>
      </div>
    </div>
    
    <!-- Hover glow effect -->
    <div class="absolute inset-0 rounded-lg bg-accent/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'

interface Skill {
  name: string
  level: string
  category?: string
}

const props = defineProps<{
  skill: Skill
}>()

const cardRef = ref(null)
const progressRef = ref(null)

onMounted(() => {
  // Animate progress bar on mount
  if (progressRef.value) {
    gsap.to(progressRef.value, {
      scaleX: 1,
      duration: 1,
      delay: Math.random() * 0.5,
      ease: 'power2.out'
    })
  }
})

const handleHover = () => {
  if (cardRef.value) {
    gsap.to(cardRef.value, {
      y: -3,
      duration: 0.3,
      ease: 'power2.out'
    })
  }
}

const handleLeave = () => {
  if (cardRef.value) {
    gsap.to(cardRef.value, {
      y: 0,
      duration: 0.3,
      ease: 'power2.out'
    })
  }
}
</script>