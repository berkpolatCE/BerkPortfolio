<template>
  <div v-if="project">
    <!-- Hero section -->
    <section class="pt-20 pb-12 bg-secondary/30">
      <div class="container mx-auto px-6">
        <a href="/projects" class="inline-flex items-center text-text-secondary hover:text-accent mb-6 transition-colors">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          Back to projects
        </a>
        
        <h1 class="font-display text-4xl md:text-5xl font-bold mb-4">{{ project.title }}</h1>
        <p class="text-text-secondary text-lg mb-8">{{ project.description }}</p>
        
        <!-- Project meta -->
        <div class="flex flex-wrap gap-6 text-sm">
          <div v-if="project.duration">
            <span class="text-text-secondary">Duration:</span>
            <span class="ml-2">{{ project.duration }}</span>
          </div>
          <div v-if="project.role">
            <span class="text-text-secondary">Role:</span>
            <span class="ml-2">{{ project.role }}</span>
          </div>
          <div v-if="project.status">
            <span class="text-text-secondary">Status:</span>
            <span class="ml-2 capitalize">{{ project.status }}</span>
          </div>
        </div>
      </div>
    </section>
    
    <!-- Project content -->
    <section class="py-16">
      <div class="container mx-auto px-6">
        <div class="max-w-4xl mx-auto">
          <!-- Project image -->
          <div v-if="project.image" class="mb-12 rounded-xl overflow-hidden">
            <img :src="project.image" :alt="project.title" class="w-full h-auto" />
          </div>
          
          <!-- Technologies -->
          <div v-if="project.technologies?.length" class="mb-12">
            <h2 class="text-2xl font-display font-semibold mb-6">Technologies Used</h2>
            <div class="flex flex-wrap gap-3">
              <span 
                v-for="tech in project.technologies" 
                :key="tech"
                class="px-4 py-2 bg-secondary rounded-lg text-sm"
              >
                {{ tech }}
              </span>
            </div>
          </div>
          
          <!-- Challenges -->
          <div v-if="project.challenges?.length" class="mb-12">
            <h2 class="text-2xl font-display font-semibold mb-6">Challenges & Solutions</h2>
            <div class="space-y-6">
              <div v-for="(challenge, index) in project.challenges" :key="index" class="bg-secondary rounded-lg p-6">
                <h3 class="font-semibold mb-2">{{ challenge.title }}</h3>
                <p class="text-text-secondary">{{ challenge.solution }}</p>
              </div>
            </div>
          </div>
          
          <!-- Links -->
          <div class="flex gap-4">
            <a 
              v-if="project.live_url"
              :href="project.live_url"
              target="_blank"
              class="inline-flex items-center gap-2 bg-accent text-primary px-6 py-3 rounded-lg font-semibold hover:bg-accent/90 transition-all duration-300"
            >
              View Live
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
            </a>
            <a 
              v-if="project.github_url"
              :href="project.github_url"
              target="_blank"
              class="inline-flex items-center gap-2 border-2 border-text-secondary text-text-secondary px-6 py-3 rounded-lg font-semibold hover:border-accent hover:text-accent transition-all duration-300"
            >
              View Code
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const projectId = route.params.id as string

// Fetch project details
const { data: project } = await useAsyncData(
  `project-${projectId}`, 
  () => useApi().getProject(projectId)
)

if (!project.value) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Project not found'
  })
}

useHead({
  title: `${project.value.title} - Portfolio`
})
</script>