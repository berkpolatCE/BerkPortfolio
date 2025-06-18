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
      
      <!-- Projects grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <ProjectCard 
          v-for="project in projects" 
          :key="project.id"
          :project="project"
          class="project-card"
        />
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
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { onMounted, computed } from 'vue'

// Fetch featured projects
const { data: projectsData } = await useAsyncData('featured-projects', () => useApi().getProjects(true))
const projects = computed(() => projectsData.value?.projects || [])

onMounted(() => {
  // Animate section title
  gsap.from('.section-title', {
    scrollTrigger: {
      trigger: '.section-title',
      start: 'top 80%'
    },
    y: 30,
    opacity: 0,
    duration: 1
  })
  
  // Animate project cards
  gsap.from('.project-card', {
    scrollTrigger: {
      trigger: '.project-card',
      start: 'top 80%'
    },
    y: 50,
    opacity: 0,
    duration: 0.8,
    stagger: 0.2
  })
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