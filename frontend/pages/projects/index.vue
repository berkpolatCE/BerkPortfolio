<template>
  <div class="min-h-screen py-16 bg-gray-50 dark:bg-dark-bg">
    <div class="max-container section-padding">
      <SectionTitle 
        title="All Projects"
        subtitle="A comprehensive showcase of my work"
        class="mb-12"
      />
      
      <!-- Filter Buttons -->
      <div class="flex justify-center mb-12">
        <div class="inline-flex rounded-lg glass-card p-1">
          <button
            @click="showFeaturedOnly = false"
            :class="[
              'px-6 py-2 rounded-lg font-medium transition-all duration-200',
              !showFeaturedOnly 
                ? 'bg-primary-600 text-white' 
                : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800'
            ]"
          >
            All Projects
          </button>
          
          <button
            @click="showFeaturedOnly = true"
            :class="[
              'px-6 py-2 rounded-lg font-medium transition-all duration-200',
              showFeaturedOnly 
                ? 'bg-primary-600 text-white' 
                : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800'
            ]"
          >
            Featured Only
          </button>
        </div>
      </div>
      
      <ProjectGrid 
        :projects="filteredProjects" 
        :loading="pending" 
      />
    </div>
  </div>
</template>

<script setup lang="ts">
const api = useApi()
const showFeaturedOnly = ref(false)

const { data: projects, pending } = await useAsyncData('all-projects', () => api.getProjects())

const filteredProjects = computed(() => {
  if (!projects.value) return []
  if (!showFeaturedOnly.value) return projects.value
  return projects.value.filter(p => p.featured)
})

// Page metadata
useHead({
  title: 'Projects'
})
</script>