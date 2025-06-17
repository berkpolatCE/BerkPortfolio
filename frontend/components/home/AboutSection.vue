<template>
  <div class="grid md:grid-cols-2 gap-12 items-center">
    <!-- Image Side -->
    <div class="relative group">
      <div v-if="loading" class="skeleton aspect-square rounded-2xl"></div>
      
      <div v-else class="relative overflow-hidden rounded-2xl shadow-2xl hover-lift">
        <NuxtImg
          :src="data?.image_url || '/api/placeholder/600/600'"
          :alt="data?.name"
          loading="lazy"
          class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700"
          width="600"
          height="600"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
      </div>
    </div>
    
    <!-- Content Side -->
    <div class="space-y-6">
      <div v-if="loading" class="space-y-4">
        <div class="skeleton h-12 w-48"></div>
        <div class="skeleton h-32 w-full"></div>
        <div class="skeleton h-20 w-full"></div>
      </div>
      
      <div v-else-if="data" class="space-y-6 animate-fade-up">
        <h2 class="text-4xl font-display font-bold gradient-text">
          About Me
        </h2>
        
        <p class="text-lg text-gray-600 dark:text-gray-300 leading-relaxed">
          {{ data.about }}
        </p>
        
        <div class="space-y-4">
          <div v-if="data.interests?.length">
            <h3 class="text-xl font-semibold mb-3">Interests</h3>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="interest in data.interests"
                :key="interest"
                class="px-4 py-2 bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300 rounded-full text-sm font-medium"
              >
                {{ interest }}
              </span>
            </div>
          </div>
        </div>
        
        <div class="pt-4">
          <a
            href="#"
            class="inline-flex items-center space-x-2 text-primary-600 dark:text-primary-400 hover:underline font-medium"
          >
            <span>Download My CV</span>
            <Icon name="heroicons:arrow-down-tray" class="w-5 h-5" />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { HomeData } from '~/composables/useApi'

interface Props {
  data?: HomeData
  loading?: boolean
}

defineProps<Props>()
</script>