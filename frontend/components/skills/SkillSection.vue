<template>
  <div v-if="loading" class="space-y-8">
    <div v-for="i in 3" :key="i" class="space-y-4">
      <div class="skeleton h-8 w-32"></div>
      <div class="grid md:grid-cols-2 gap-4">
        <div v-for="j in 4" :key="j" class="skeleton h-16"></div>
      </div>
    </div>
  </div>
  
  <div v-else-if="skills" class="space-y-12">
    <!-- Technical Skills -->
    <div v-if="skills.technical" class="space-y-8">
      <div 
        v-for="(items, category) in skills.technical" 
        :key="category"
        class="animate-fade-up"
      >
        <h3 class="text-2xl font-semibold capitalize mb-6 text-gray-900 dark:text-white">
          {{ category }}
        </h3>
        
        <div class="grid md:grid-cols-2 gap-6">
          <SkillBar
            v-for="skill in items"
            :key="skill.name"
            :skill="skill"
          />
        </div>
      </div>
    </div>
    
    <!-- Soft Skills -->
    <div v-if="skills.soft?.length" class="animate-fade-up">
      <h3 class="text-2xl font-semibold mb-6 text-gray-900 dark:text-white">
        Soft Skills
      </h3>
      
      <div class="flex flex-wrap gap-3">
        <span
          v-for="skill in skills.soft"
          :key="skill"
          class="px-6 py-3 glass-card rounded-full text-gray-700 dark:text-gray-300 font-medium hover:shadow-lg transition-all duration-200 hover:-translate-y-1"
        >
          {{ skill }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { SkillsData } from '~/composables/useApi'

interface Props {
  skills?: SkillsData
  loading?: boolean
}

defineProps<Props>()
</script>