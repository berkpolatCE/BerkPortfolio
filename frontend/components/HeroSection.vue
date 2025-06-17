<template>
  <section class="relative min-h-screen flex items-center justify-center overflow-hidden">
    <!-- Background gradient -->
    <div class="absolute inset-0 bg-gradient-to-br from-primary via-secondary to-primary opacity-50"></div>
    
    <!-- Animated particles -->
    <div class="particles absolute inset-0"></div>
    
    <div class="container mx-auto px-6 relative z-10">
      <div class="max-w-4xl mx-auto text-center">
        <!-- Name with animation -->
        <h1 ref="heroTitle" class="font-display text-5xl md:text-7xl lg:text-8xl font-bold mb-6 opacity-0">
          <span class="inline-block" v-for="(word, i) in titleWords" :key="i">
            {{ word }}&nbsp;
          </span>
        </h1>
        
        <!-- Title/Tagline -->
        <p ref="heroTagline" class="text-xl md:text-2xl text-text-secondary mb-12 opacity-0">
          {{ homeData?.title || 'Loading...' }}
        </p>
        
        <!-- CTA Buttons -->
        <div ref="heroCta" class="flex flex-col sm:flex-row gap-4 justify-center opacity-0">
          <a href="#projects" class="btn-primary">
            View Projects
          </a>
          <a href="#contact" class="btn-secondary">
            Get in Touch
          </a>
        </div>
        
        <!-- Scroll indicator -->
        <div ref="scrollIndicator" class="absolute bottom-8 left-1/2 transform -translate-x-1/2 opacity-0">
          <div class="mouse-scroll">
            <div class="mouse">
              <div class="wheel"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { gsap } from 'gsap'
import { onMounted, ref, computed } from 'vue'

const heroTitle = ref(null)
const heroTagline = ref(null)
const heroCta = ref(null)
const scrollIndicator = ref(null)

// Fetch home data
const { data: homeData } = await useAsyncData('home', () => useApi().getHome())

const titleWords = computed(() => {
  const name = homeData.value?.name || 'Loading'
  return name.split(' ')
})

onMounted(() => {
  // Create timeline for hero animations
  const tl = gsap.timeline({ defaults: { ease: 'power3.out' } })
  
  // Animate title words
  const titleChars = heroTitle.value?.querySelectorAll('.inline-block')
  tl.set(titleChars, { y: 50, opacity: 0 })
    .to(titleChars, {
      y: 0,
      opacity: 1,
      duration: 1,
      stagger: 0.1
    })
    .to(heroTagline.value, {
      opacity: 1,
      y: 0,
      duration: 0.8
    }, '-=0.5')
    .to(heroCta.value, {
      opacity: 1,
      y: 0,
      duration: 0.8
    }, '-=0.5')
    .to(scrollIndicator.value, {
      opacity: 0.7,
      duration: 1
    }, '-=0.3')
  
  // Particle animation
  createParticles()
})

function createParticles() {
  const particlesContainer = document.querySelector('.particles')
  if (!particlesContainer) return
  
  for (let i = 0; i < 50; i++) {
    const particle = document.createElement('div')
    particle.className = 'particle'
    particle.style.left = `${Math.random() * 100}%`
    particle.style.top = `${Math.random() * 100}%`
    particle.style.animationDelay = `${Math.random() * 20}s`
    particle.style.animationDuration = `${20 + Math.random() * 20}s`
    particlesContainer.appendChild(particle)
  }
}
</script>

<style scoped>
.btn-primary {
  @apply px-8 py-4 bg-accent text-primary font-semibold rounded-lg transition-all duration-300 hover:bg-accent/90 hover:scale-105 hover:shadow-xl hover:shadow-accent/20;
}

.btn-secondary {
  @apply px-8 py-4 border-2 border-text-secondary text-text-secondary font-semibold rounded-lg transition-all duration-300 hover:border-accent hover:text-accent hover:scale-105;
}

.particle {
  position: absolute;
  width: 2px;
  height: 2px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  animation: float 20s infinite ease-in-out;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) translateX(0);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    transform: translateY(-100vh) translateX(100px);
    opacity: 0;
  }
}

.mouse-scroll {
  @apply relative;
}

.mouse {
  @apply w-6 h-10 border-2 border-text-secondary rounded-full relative;
}

.wheel {
  @apply w-1 h-2 bg-text-secondary rounded-full absolute left-1/2 transform -translate-x-1/2 top-2;
  animation: scroll 2s infinite;
}

@keyframes scroll {
  0% {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
  }
  100% {
    transform: translateX(-50%) translateY(15px);
    opacity: 0;
  }
}
</style>