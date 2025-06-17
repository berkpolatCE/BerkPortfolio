<template>
  <article class="group glass-card rounded-xl overflow-hidden hover-lift hover-glow">
    <!-- Image -->
    <div class="relative aspect-[16/9] overflow-hidden bg-gray-100 dark:bg-gray-800">
      <NuxtImg
        :src="project.image || '/api/placeholder/400/300'"
        :alt="project.title"
        loading="lazy"
        class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700"
        width="400"
        height="300"
      />
      
      <!-- Overlay -->
      <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6">
        <div class="flex space-x-3">
          <a
            v-if="project.github_url"
            :href="project.github_url"
            target="_blank"
            rel="noopener noreferrer"
            class="p-2 bg-white/20 backdrop-blur-sm rounded-lg text-white hover:bg-white/30 transition-colors duration-200"
            aria-label="View on GitHub"
          >
            <Icon name="mdi:github" class="w-5 h-5" />
          </a>
          
          <a
            v-if="project.live_url"
            :href="project.live_url"
            target="_blank"
            rel="noopener noreferrer"
            class="p-2 bg-white/20 backdrop-blur-sm rounded-lg text-white hover:bg-white/30 transition-colors duration-200"
            aria-label="View live demo"
          >
            <Icon name="heroicons:arrow-top-right-on-square" class="w-5 h-5" />
          </a>
        </div>
      </div>
    </div>
    
    <!-- Content -->
    <div class="p-6 space-y-4">
      <h3 class="text-xl font-semibold text-gray-900 dark:text-white group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors duration-200">
        {{ project.title }}
      </h3>
      
      <p class="text-gray-600 dark:text-gray-300 line-clamp-2">
        {{ project.description }}
      </p>
      
      <!-- Technologies -->
      <div class="flex flex-wrap gap-2">
        <span
          v-for="tech in project.technologies.slice(0, 3)"
          :key="tech"
          class="px-3 py-1 bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 rounded-full text-xs font-medium"
        >
          {{ tech }}
        </span>
        <span
          v-if="project.technologies.length > 3"
          class="px-3 py-1 text-gray-500 dark:text-gray-400 text-xs"
        >
          +{{ project.technologies.length - 3 }} more
        </span>
      </div>
      
      <NuxtLink
        :to="`/projects/${project.id}`"
        class="inline-flex items-center space-x-1 text-primary-600 dark:text-primary-400 hover:underline font-medium text-sm"
      >
        <span>View Details</span>
        <Icon name="heroicons:arrow-right" class="w-4 h-4" />
      </NuxtLink>
    </div>
  </article>
</template>

<script setup lang="ts">
import type { Project } from '~/composables/useApi'

interface Props {
  project: Project
}

defineProps<Props>()
</script>