<template>
  <div 
    ref="categoryRef"
    @click="$emit('click')"
    class="skill-category-card relative cursor-pointer select-none"
    :class="{ 'is-expanded': isExpanded }"
  >
    <!-- Category Card -->
    <div class="category-box relative bg-primary border-2 border-border rounded-xl p-6 transition-all duration-500"
         :class="{ 
           'border-accent shadow-lg shadow-accent/20': isExpanded,
           'hover:border-accent/50': !isExpanded
         }">
      
      <!-- Icon -->
      <div class="category-icon w-16 h-16 mx-auto mb-4 rounded-xl flex items-center justify-center transition-all duration-500"
           :class="[
             isExpanded ? 'bg-accent/20' : 'bg-secondary',
             `category-${category.id}`
           ]">
        <!-- Programming Icon -->
        <svg v-if="category.id === 'programming'" class="w-8 h-8 transition-colors duration-500"
             :class="isExpanded ? 'text-accent' : 'text-text-secondary'"
             fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path>
        </svg>
        
        <!-- Frameworks Icon -->
        <svg v-else-if="category.id === 'frameworks'" class="w-8 h-8 transition-colors duration-500"
             :class="isExpanded ? 'text-accent' : 'text-text-secondary'"
             fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
        </svg>
        
        <!-- Cybersecurity Icon -->
        <svg v-else-if="category.id === 'cybersecurity'" class="w-8 h-8 transition-colors duration-500"
             :class="isExpanded ? 'text-accent' : 'text-text-secondary'"
             fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
        </svg>
        
        <!-- General Icon -->
        <svg v-else class="w-8 h-8 transition-colors duration-500"
             :class="isExpanded ? 'text-accent' : 'text-text-secondary'"
             fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
        </svg>
      </div>
      
      <!-- Category Name -->
      <h3 class="text-lg font-display font-semibold text-center mb-2 transition-colors duration-500"
          :class="isExpanded ? 'text-accent' : 'text-text-primary'">
        {{ category.name }}
      </h3>
      
      <!-- Skill Count -->
      <p class="text-sm text-text-secondary text-center">
        {{ category.skills.length }} skills
      </p>
      
      <!-- Expand/Collapse Indicator -->
      <div class="absolute -bottom-3 left-1/2 transform -translate-x-1/2">
        <div class="w-6 h-6 bg-primary border-2 rounded-full flex items-center justify-center transition-all duration-500"
             :class="isExpanded ? 'border-accent rotate-180' : 'border-border'">
          <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </div>
    </div>

    <!-- Glow Effect -->
    <div v-if="isExpanded" class="absolute inset-0 rounded-xl bg-accent/10 blur-xl -z-10 animate-pulse"></div>
  </div>
</template>
  
<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { gsap } from 'gsap'

interface CategorySkill {
  name: string
  level: string
}

interface Category {
  id: string
  name: string
  skills: CategorySkill[]
  icon?: string
}

const props = defineProps<{
  category: Category
  isExpanded: boolean
}>()

defineEmits<{
  click: []
}>()

const categoryRef = ref(null)

// Track if animation is in progress
let isAnimating = false

// Hover animation
onMounted(() => {
  if (categoryRef.value) {
    gsap.set(categoryRef.value, { scale: 1 })
    
    categoryRef.value.addEventListener('mouseenter', () => {
      if (!props.isExpanded && !isAnimating) {
        gsap.to(categoryRef.value, {
          scale: 1.05,
          duration: 0.2,
          ease: 'power2.out'
        })
      }
    })
    
    categoryRef.value.addEventListener('mouseleave', () => {
      if (!props.isExpanded && !isAnimating) {
        gsap.to(categoryRef.value, {
          scale: 1,
          duration: 0.2,
          ease: 'power2.out'
        })
      }
    })
  }
})

// Watch for expansion changes
watch(() => props.isExpanded, (newVal, oldVal) => {
  if (newVal !== oldVal && categoryRef.value) {
    isAnimating = true
    
    // Reset scale when expanding/collapsing
    gsap.to(categoryRef.value, {
      scale: 1,
      duration: 0.2,
      ease: 'power2.out',
      onComplete: () => {
        isAnimating = false
      }
    })
  }
})
</script>

<style scoped>
.skill-category-card {
  @apply relative;
}

.category-programming {
  background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
}

.category-frameworks {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
}

.category-cybersecurity {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
}

.category-general {
  background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
}
</style>