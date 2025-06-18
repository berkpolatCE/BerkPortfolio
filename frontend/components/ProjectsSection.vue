<template>
  <section id="projects" class="py-20 md:py-32">
    <div class="container mx-auto px-6">
      <!-- Section header -->
      <div class="text-center mb-16">
        <h2 class="section-title">
          Featured Projects
        </h2>
        <p class="text-text-secondary text-lg max-w-2xl mx-auto">
          A selection of my recent work and side projects
        </p>
      </div>
      
      <!-- Loading state -->
      <div v-if="pending" class="flex justify-center items-center min-h-[400px]">
        <div class="animate-pulse">
          <div class="w-16 h-16 border-4 border-accent border-t-transparent rounded-full animate-spin"></div>
        </div>
      </div>
      
      <!-- Error state -->
      <div v-else-if="error" class="text-center py-12">
        <p class="text-red-400 mb-4">Failed to load projects</p>
        <button 
          @click="refresh()" 
          class="px-6 py-2 bg-accent text-primary rounded-lg hover:bg-accent/80 transition-colors"
        >
          Retry
        </button>
      </div>
      
      <!-- Projects grid -->
      <div v-else-if="projects.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <ProjectCard 
          v-for="project in projects" 
          :key="project.id"
          :project="project"
          class="project-card"
        />
      </div>
      
      <!-- Empty state -->
      <div v-else class="text-center py-12">
        <p class="text-text-secondary">No projects available at the moment.</p>
      </div>
      
      <!-- View all link -->
      <div class="text-center mt-12">
        <NuxtLink to="/projects" class="inline-flex items-center text-accent hover:text-accent/80 transition-colors">
          View All Projects
          <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </NuxtLink>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted, computed, watch, nextTick } from 'vue'

// Use our animation composable
const { animateOnScroll } = useGSAPAnimation()

// Fetch featured projects with better error handling
const { data: projectsData, pending, error, refresh } = await useAsyncData(
  'featured-projects', 
  async () => {
    try {
      return await useApi().getProjects(true)
    } catch (err) {
      console.error('[ProjectsSection] Failed to fetch projects:', err)
      // Return empty array as fallback
      return { projects: [] }
    }
  },
  {
    lazy: false,
    server: true,
    default: () => ({ projects: [] })
  }
)

const projects = computed(() => projectsData.value?.projects || [])

// Watch for when data is loaded and then animate
watch(() => pending.value, (isPending) => {
  if (!isPending && projects.value.length > 0) {
    // Use nextTick to ensure DOM is updated
    nextTick(() => {
      animateOnScroll('.section-title', {
        y: 30,
        stagger: 0
      })
      animateOnScroll('.project-card')
    })
  }
}, { immediate: true })

// Also animate on mount in case data is already loaded
onMounted(() => {
  if (!pending.value && projects.value.length > 0) {
    animateOnScroll('.section-title', {
      y: 30,
      stagger: 0
    })
    animateOnScroll('.project-card')
  }
})
</script>

<style scoped>
.section-title {
  @apply font-display text-4xl md:text-5xl font-bold mb-4;
  background: linear-gradient(to right, #ffffff 0%, #a3a3a3 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
</style>