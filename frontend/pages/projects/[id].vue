<template>
  <div class="min-h-screen py-16 bg-white dark:bg-dark-bg">
    <div class="max-container section-padding">
      <!-- Back Button -->
      <NuxtLink
        to="/projects"
        class="inline-flex items-center space-x-2 text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 mb-8 transition-colors duration-200"
      >
        <Icon name="heroicons:arrow-left" class="w-5 h-5" />
        <span>Back to Projects</span>
      </NuxtLink>
      
      <div v-if="pending" class="space-y-8">
        <div class="skeleton h-12 w-2/3"></div>
        <div class="skeleton aspect-video rounded-xl"></div>
        <div class="skeleton h-32 w-full"></div>
      </div>
      
      <div v-else-if="project" class="space-y-8 animate-fade-up">
        <!-- Header -->
        <div class="text-center space-y-4">
          <h1 class="text-4xl md:text-5xl font-display font-bold gradient-text">
            {{ project.title }}
          </h1>
          
          <div class="flex justify-center space-x-4">
            <a
              v-if="project.github_url"
              :href="project.github_url"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center space-x-2 px-6 py-3 glass-card rounded-lg hover:shadow-lg transition-all duration-200 hover-lift"
            >
              <Icon name="mdi:github" class="w-5 h-5" />
              <span>View Code</span>
            </a>
            
            <a
              v-if="project.live_url"
              :href="project.live_url"
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center space-x-2 px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-all duration-200 hover-lift"
            >
              <Icon name="heroicons:arrow-top-right-on-square" class="w-5 h-5" />
              <span>Live Demo</span>
            </a>
          </div>
        </div>
        
        <!-- Project Image -->
        <div class="relative aspect-video rounded-xl overflow-hidden shadow-2xl">
          <NuxtImg
            :src="project.image || '/api/placeholder/1200/675'"
            :alt="project.title"
            loading="lazy"
            class="w-full h-full object-cover"
            width="1200"
            height="675"
          />
        </div>
        
        <!-- Description -->
        <div class="prose prose-lg dark:prose-invert max-w-3xl mx-auto">
          <p>{{ project.description }}</p>
        </div>
        
        <!-- Technologies -->
        <div class="max-w-3xl mx-auto">
          <h2 class="text-2xl font-semibold mb-6">Technologies Used</h2>
          <div class="flex flex-wrap gap-3">
            <span
              v-for="tech in project.technologies"
              :key="tech"
              class="px-6 py-3 glass-card rounded-full font-medium hover:shadow-lg transition-all duration-200 hover:-translate-y-1"
            >
              {{ tech }}
            </span>
          </div>
        </div>
      </div>
      
      <div v-else class="text-center py-16">
        <Icon name="heroicons:exclamation-triangle" class="w-16 h-16 text-gray-400 mb-4" />
        <p class="text-xl text-gray-600 dark:text-gray-400">Project not found</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const api = useApi()

const projectId = computed(() => parseInt(route.params.id as string))

const { data: project, pending, error } = await useAsyncData(
  `project-${projectId.value}`,
  () => api.getProject(projectId.value)
)

// Page metadata
useHead({
  title: () => project.value ? project.value.title : 'Project Details'
})

// Handle 404
if (error.value) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Project not found'
  })
}
</script>