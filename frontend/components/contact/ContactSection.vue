<template>
  <div class="text-center">
    <div v-if="loading" class="space-y-6">
      <div class="skeleton h-8 w-64 mx-auto"></div>
      <div class="skeleton h-32 w-full max-w-2xl mx-auto"></div>
      <div class="flex justify-center space-x-4">
        <div v-for="i in 4" :key="i" class="skeleton w-12 h-12 rounded-full"></div>
      </div>
    </div>
    
    <div v-else-if="contact" class="space-y-8 animate-fade-up">
      <p class="text-xl text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
        I'm {{ contact.availability }}. Feel free to reach out for collaborations, opportunities, or just to say hello!
      </p>
      
      <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
        <a
          :href="`mailto:${contact.email}`"
          class="flex items-center space-x-3 px-6 py-3 glass-card rounded-lg hover:shadow-lg transition-all duration-200 hover-lift"
        >
          <Icon name="heroicons:envelope" class="w-5 h-5 text-primary-600" />
          <span>{{ contact.email }}</span>
        </a>
        
        <a
          v-if="contact.phone"
          :href="`tel:${contact.phone}`"
          class="flex items-center space-x-3 px-6 py-3 glass-card rounded-lg hover:shadow-lg transition-all duration-200 hover-lift"
        >
          <Icon name="heroicons:phone" class="w-5 h-5 text-primary-600" />
          <span>{{ contact.phone }}</span>
        </a>
      </div>
      
      <div class="flex justify-center space-x-6 pt-8">
        <a
          v-if="contact.github"
          :href="contact.github"
          target="_blank"
          rel="noopener noreferrer"
          class="p-4 glass-card rounded-full hover:shadow-lg transition-all duration-200 hover-lift group"
          aria-label="GitHub"
        >
          <Icon name="mdi:github" class="w-8 h-8 text-gray-700 dark:text-gray-300 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors duration-200" />
        </a>
        
        <a
          v-if="contact.linkedin"
          :href="contact.linkedin"
          target="_blank"
          rel="noopener noreferrer"
          class="p-4 glass-card rounded-full hover:shadow-lg transition-all duration-200 hover-lift group"
          aria-label="LinkedIn"
        >
          <Icon name="mdi:linkedin" class="w-8 h-8 text-gray-700 dark:text-gray-300 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors duration-200" />
        </a>
        
        <a
          v-if="contact.twitter"
          :href="contact.twitter"
          target="_blank"
          rel="noopener noreferrer"
          class="p-4 glass-card rounded-full hover:shadow-lg transition-all duration-200 hover-lift group"
          aria-label="Twitter"
        >
          <Icon name="mdi:twitter" class="w-8 h-8 text-gray-700 dark:text-gray-300 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors duration-200" />
        </a>
        
        <a
          v-if="contact.instagram"
          :href="contact.instagram"
          target="_blank"
          rel="noopener noreferrer"
          class="p-4 glass-card rounded-full hover:shadow-lg transition-all duration-200 hover-lift group"
          aria-label="Instagram"
        >
          <Icon name="mdi:instagram" class="w-8 h-8 text-gray-700 dark:text-gray-300 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors duration-200" />
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { ContactData } from '~/composables/useApi'

interface Props {
  contact?: ContactData
  loading?: boolean
}

defineProps<Props>()
</script>