<template>
  <footer class="bg-gray-100 dark:bg-dark-card border-t border-gray-200 dark:border-dark-border">
    <div class="max-container section-padding py-8">
      <div class="flex flex-col md:flex-row items-center justify-between space-y-4 md:space-y-0">
        <div class="text-center md:text-left">
          <p class="text-gray-600 dark:text-gray-400">
            © {{ currentYear }} Portfolio. All rights reserved.
          </p>
        </div>
        
        <div class="flex items-center space-x-6">
          <a
            v-for="social in socials"
            :key="social.name"
            :href="social.url"
            target="_blank"
            rel="noopener noreferrer"
            class="text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors duration-200"
            :aria-label="social.name"
          >
            <Icon :name="social.icon" class="w-6 h-6" />
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const currentYear = new Date().getFullYear()

// This will be populated with actual data from the API
const socials = [
  { name: 'GitHub', icon: 'mdi:github', url: 'https://github.com' },
  { name: 'LinkedIn', icon: 'mdi:linkedin', url: 'https://linkedin.com' },
  { name: 'Twitter', icon: 'mdi:twitter', url: 'https://twitter.com' },
]
</script>