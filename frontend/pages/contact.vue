<template>
  <div class="min-h-screen py-16 bg-gradient-to-br from-primary-50 to-purple-50 dark:from-dark-bg dark:to-dark-card">
    <div class="max-container section-padding">
      <SectionTitle 
        title="Let's Connect"
        subtitle="I'm always open to discussing new opportunities and interesting projects"
        class="mb-16"
      />
      
      <div class="max-w-4xl mx-auto">
        <div class="glass-card rounded-2xl p-8 md:p-12 shadow-xl">
          <div v-if="pending" class="space-y-8">
            <div class="skeleton h-32 w-full"></div>
            <div class="skeleton h-24 w-full"></div>
          </div>
          
          <div v-else-if="contact" class="space-y-12 animate-fade-up">
            <!-- Contact Info Grid -->
            <div class="grid md:grid-cols-2 gap-8">
              <a
                :href="`mailto:${contact.email}`"
                class="group flex items-start space-x-4 p-6 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 transition-all duration-200"
              >
                <div class="p-3 bg-primary-100 dark:bg-primary-900/30 rounded-lg group-hover:scale-110 transition-transform duration-200">
                  <Icon name="heroicons:envelope" class="w-6 h-6 text-primary-600 dark:text-primary-400" />
                </div>
                <div>
                  <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Email</h3>
                  <p class="text-gray-600 dark:text-gray-300">{{ contact.email }}</p>
                </div>
              </a>
              
              <a
                v-if="contact.phone"
                :href="`tel:${contact.phone}`"
                class="group flex items-start space-x-4 p-6 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 transition-all duration-200"
              >
                <div class="p-3 bg-primary-100 dark:bg-primary-900/30 rounded-lg group-hover:scale-110 transition-transform duration-200">
                  <Icon name="heroicons:phone" class="w-6 h-6 text-primary-600 dark:text-primary-400" />
                </div>
                <div>
                  <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Phone</h3>
                  <p class="text-gray-600 dark:text-gray-300">{{ contact.phone }}</p>
                </div>
              </a>
            </div>
            
            <!-- Social Links -->
            <div>
              <h3 class="text-xl font-semibold text-center mb-8">Find me on social media</h3>
              
              <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <a
                  v-if="contact.github"
                  :href="contact.github"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="group flex flex-col items-center p-6 glass-card rounded-xl hover:shadow-lg transition-all duration-200 hover-lift"
                >
                  <Icon name="mdi:github" class="w-12 h-12 text-gray-700 dark:text-gray-300 group-hover:text-primary-600 dark:group-hover:text-primary-400 mb-3 transition-colors duration-200" />
                  <span class="font-medium">GitHub</span>
                </a>
                
                <a
                  v-if="contact.linkedin"
                  :href="contact.linkedin"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="group flex flex-col items-center p-6 glass-card rounded-xl hover:shadow-lg transition-all duration-200 hover-lift"
                >
                  <Icon name="mdi:linkedin" class="w-12 h-12 text-gray-700 dark:text-gray-300 group-hover:text-primary-600 dark:group-hover:text-primary-400 mb-3 transition-colors duration-200" />
                  <span class="font-medium">LinkedIn</span>
                </a>
                
                <a
                  v-if="contact.twitter"
                  :href="contact.twitter"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="group flex flex-col items-center p-6 glass-card rounded-xl hover:shadow-lg transition-all duration-200 hover-lift"
                >
                  <Icon name="mdi:twitter" class="w-12 h-12 text-gray-700 dark:text-gray-300 group-hover:text-primary-600 dark:group-hover:text-primary-400 mb-3 transition-colors duration-200" />
                  <span class="font-medium">Twitter</span>
                </a>
                
                <a
                  v-if="contact.instagram"
                  :href="contact.instagram"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="group flex flex-col items-center p-6 glass-card rounded-xl hover:shadow-lg transition-all duration-200 hover-lift"
                >
                  <Icon name="mdi:instagram" class="w-12 h-12 text-gray-700 dark:text-gray-300 group-hover:text-primary-600 dark:group-hover:text-primary-400 mb-3 transition-colors duration-200" />
                  <span class="font-medium">Instagram</span>
                </a>
              </div>
            </div>
            
            <!-- Availability Status -->
            <div class="text-center p-6 bg-gradient-to-r from-primary-100 to-purple-100 dark:from-primary-900/20 dark:to-purple-900/20 rounded-xl">
              <p class="text-lg font-medium text-gray-900 dark:text-white">
                Current Status: <span class="text-primary-600 dark:text-primary-400">{{ contact.availability }}</span>
              </p>
            </div>
          </div>
        </div>
        
        <!-- CV Download Section -->
        <div v-if="cvData" class="mt-12 text-center animate-fade-up" style="animation-delay: 200ms">
          <h3 class="text-xl font-semibold mb-4">Download My Resume</h3>
          <a
            :href="`${$config.public.apiBase}/cv/download`"
            class="inline-flex items-center space-x-3 px-8 py-4 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-all duration-200 hover-lift"
          >
            <Icon name="heroicons:document-arrow-down" class="w-6 h-6" />
            <span>Download CV (PDF)</span>
          </a>
          <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
            Last updated: {{ formatDate(cvData.last_updated) }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const api = useApi()

const { data: contact, pending } = await useAsyncData('contact', () => api.getContact())
const { data: cvData } = await useAsyncData('cv', () => api.getCv())

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

// Page metadata
useHead({
  title: 'Contact'
})
</script>