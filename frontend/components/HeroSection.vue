<template>
  <section class="relative min-h-screen flex items-center justify-center overflow-hidden">
    <!-- Background gradient -->
    <div class="absolute inset-0 bg-gradient-to-br from-primary via-secondary to-primary opacity-50"></div>
    
    <!-- Animated particles -->
    <div class="particles absolute inset-0"></div>
    
    <div class="container mx-auto px-6 relative z-10">
      <div class="max-w-4xl mx-auto text-center">
        <!-- Profile Photo -->
        <div ref="profilePhoto" class="mb-8 opacity-0">
          <div class="relative inline-block">
            <div class="w-32 h-32 md:w-40 md:h-40 rounded-full overflow-hidden border-4 border-accent/30 shadow-2xl relative z-10">
              <img 
                :src="getProfileImage()" 
                :alt="homeData?.name || 'Profile'"
                class="w-full h-full object-cover"
              />
            </div>
            <!-- Decorative ring -->
            <div class="absolute inset-0 rounded-full border-2 border-accent/20 animate-pulse scale-110"></div>
            <div class="absolute inset-0 rounded-full border-2 border-accent/10 animate-ping"></div>
          </div>
        </div>
        
        <!-- Name with animation -->
        <h1 ref="heroTitle" class="font-display text-5xl md:text-7xl lg:text-8xl font-bold mb-4 opacity-0">
          <span class="inline-block" v-for="(word, i) in titleWords" :key="i">
            {{ word }}&nbsp;
          </span>
        </h1>
        
        <!-- Title/Tagline -->
        <p ref="heroTagline" class="text-xl md:text-2xl text-text-secondary mb-8 opacity-0">
          {{ homeData?.title || 'Loading...' }}
        </p>
        
        <!-- Additional Info Section -->
        <div ref="heroInfo" class="max-w-3xl mx-auto mb-12 space-y-6 opacity-0">
          <!-- About -->
          <p class="text-lg text-text-secondary/90 leading-relaxed">
            {{ homeData?.about || '' }}
          </p>
          
          <!-- Info Grid -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
            <!-- Location -->
            <div class="flex items-center justify-center space-x-2">
              <svg class="w-5 h-5 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              <span class="text-text-secondary">{{ homeData?.location || '' }}</span>
            </div>
            
            <!-- Languages -->
            <div class="flex items-center justify-center space-x-2">
              <svg class="w-5 h-5 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"></path>
              </svg>
              <span class="text-text-secondary">{{ homeData?.languages?.join(', ') || '' }}</span>
            </div>
            
            <!-- Interests -->
            <div class="flex items-center justify-center space-x-2">
              <svg class="w-5 h-5 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
              </svg>
              <span class="text-text-secondary">{{ homeData?.interests?.slice(0, 2).join(', ') || '' }}</span>
            </div>
          </div>
        </div>
        
        <!-- CTA Buttons -->
        <div ref="heroCta" class="flex flex-col sm:flex-row gap-4 justify-center opacity-0">
          <a href="#projects" class="btn-primary">
            View Projects
          </a>
          <a href="#contact" class="btn-secondary">
            Get in Touch
          </a>
        </div>
        
      </div>
    </div>
    
    <!-- Scroll indicator -->
    <div ref="scrollIndicator" class="absolute bottom-20 left-1/2 transform -translate-x-1/2 opacity-0">
      <div class="mouse-scroll">
        <div class="mouse">
          <div class="wheel"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { gsap } from 'gsap'
import { onMounted, ref, computed } from 'vue'

const profilePhoto = ref(null)
const heroTitle = ref(null)
const heroTagline = ref(null)
const heroInfo = ref(null)
const heroCta = ref(null)
const scrollIndicator = ref(null)

// Fetch home data
const { data: homeData } = await useAsyncData('home', () => useApi().getHome())
const { getProfileImage } = useImages()

const titleWords = computed(() => {
  const name = homeData.value?.name || 'Loading'
  return name.split(' ')
})

onMounted(() => {
  // Create timeline for hero animations
  const tl = gsap.timeline({ defaults: { ease: 'power3.out' } })
  
  // Animate profile photo
  tl.set(profilePhoto.value, { scale: 0.8, opacity: 0 })
    .to(profilePhoto.value, {
      scale: 1,
      opacity: 1,
      duration: 1.2,
      ease: 'elastic.out(1, 0.8)'
    })
  
  // Animate title words
  const titleChars = heroTitle.value?.querySelectorAll('.inline-block')
  tl.set(titleChars, { y: 50, opacity: 0 })
    .to(titleChars, {
      y: 0,
      opacity: 1,
      duration: 1,
      stagger: 0.1
    }, '-=0.8')
    .to(heroTagline.value, {
      opacity: 1,
      y: 0,
      duration: 0.8
    }, '-=0.5')
    .to(heroInfo.value, {
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