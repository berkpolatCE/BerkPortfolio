<template>
  <section class="relative min-h-[80vh] flex items-center justify-center overflow-hidden gradient-animation">
    <div class="absolute inset-0 bg-black/10 dark:bg-black/30"></div>
    
    <div class="relative z-10 max-container section-padding py-20 text-center text-white">
      <div v-if="loading" class="space-y-4">
        <div class="skeleton h-16 w-64 mx-auto"></div>
        <div class="skeleton h-8 w-96 mx-auto"></div>
        <div class="skeleton h-24 w-full max-w-2xl mx-auto"></div>
      </div>
      
      <div v-else-if="data" class="space-y-8 animate-fade-up">
        <h1 class="text-5xl md:text-7xl font-display font-bold">
          {{ data.name }}
        </h1>
        
        <p class="text-2xl md:text-3xl font-light">
          {{ data.title }}
        </p>
        
        <div class="flex flex-wrap items-center justify-center gap-4 text-lg">
          <div class="flex items-center space-x-2">
            <Icon name="heroicons:map-pin" class="w-5 h-5" />
            <span>{{ data.location }}</span>
          </div>
          
          <div class="flex items-center space-x-2">
            <Icon name="heroicons:language" class="w-5 h-5" />
            <span>{{ data.languages.join(', ') }}</span>
          </div>
        </div>
        
        <div class="flex flex-wrap justify-center gap-4 mt-8">
          <NuxtLink
            to="/projects"
            class="px-8 py-3 bg-white text-primary-600 rounded-lg font-semibold hover:bg-gray-100 transition-all duration-200 hover-lift"
          >
            View My Work
          </NuxtLink>
          
          <NuxtLink
            to="/contact"
            class="px-8 py-3 bg-transparent border-2 border-white text-white rounded-lg font-semibold hover:bg-white hover:text-primary-600 transition-all duration-200"
          >
            Get In Touch
          </NuxtLink>
        </div>
      </div>
    </div>
    
    <!-- Scroll indicator -->
    <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
      <Icon name="heroicons:chevron-down" class="w-8 h-8 text-white" />
    </div>
  </section>
</template>

<script setup lang="ts">
import type { HomeData } from '~/composables/useApi'

interface Props {
  data?: HomeData
  loading?: boolean
}

defineProps<Props>()
</script>