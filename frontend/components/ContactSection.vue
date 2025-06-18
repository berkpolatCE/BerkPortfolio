<template>
  <section id="contact" class="py-20 md:py-32">
    <div class="container mx-auto px-6">
      <!-- Section header -->
      <div class="text-center mb-16">
        <h2 class="section-title">
          Let's Connect
        </h2>
        <p class="text-text-secondary text-lg max-w-2xl mx-auto">
          Have a project in mind? Let's discuss how we can work together.
        </p>
      </div>
      
      <!-- Contact content -->
      <div class="max-w-4xl mx-auto">
        <div class="grid md:grid-cols-2 gap-12">
          <!-- Contact info -->
          <div class="space-y-8">
            <div v-for="item in contactItems" :key="item.type" class="contact-item">
              <div class="flex items-start gap-4">
                <div class="w-12 h-12 bg-secondary rounded-lg flex items-center justify-center flex-shrink-0">
                  <component :is="item.icon" class="w-6 h-6 text-accent" />
                </div>
                <div>
                  <h3 class="font-semibold mb-1">{{ item.label }}</h3>
                  <a 
                    :href="item.href" 
                    :target="item.external ? '_blank' : '_self'"
                    class="text-text-secondary hover:text-accent transition-colors"
                  >
                    {{ item.value }}
                  </a>
                </div>
              </div>
            </div>
            
            <!-- Social links -->
            <div class="pt-8 border-t border-border">
              <h3 class="font-semibold mb-4">Find me on</h3>
              <div class="flex flex-col sm:flex-row gap-4">
                <a  
                  v-if="contactData?.github"
                  :href="contactData.github"
                  target="_blank"
                  class="inline-flex items-center gap-2 border-2 border-text-primary text-text-primary visited:text-text-primary visited:border-text-primary px-6 py-3 rounded-lg font-semibold hover:border-accent hover:text-accent transition-all duration-300"
                  aria-label="GitHub"
                >
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                  </svg>
                  GitHub
                </a>
                <a 
                  v-if="contactData?.linkedin"
                  :href="contactData.linkedin"
                  target="_blank"
                  class="inline-flex items-center gap-2 border-2 border-text-primary text-text-primary visited:text-text-primary visited:border-text-primary px-6 py-3 rounded-lg font-semibold hover:border-accent hover:text-accent transition-all duration-300"
                  aria-label="LinkedIn"
                >
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                  </svg>
                  LinkedIn
                </a>
              </div>
            </div>
          </div>
          
          <!-- Contact CTA -->
          <div class="bg-secondary rounded-2xl p-8 md:p-10">
            <h3 class="text-2xl font-display font-semibold mb-4">
              Ready to start a project?
            </h3>
            <p class="text-text-secondary mb-8">
              I'm always interested in hearing about new opportunities and exciting projects.
            </p>
            <a 
              v-if="contactData?.email"
              :href="`mailto:${contactData?.email}`" 
              class="inline-flex items-center gap-2 bg-accent text-primary px-6 py-3 rounded-lg font-semibold hover:bg-accent/90 transition-all duration-300 hover:scale-105"
            >
              Send me an email
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </a>
            <div v-else class="text-text-secondary">
              <p class="mb-2">Connect with me on:</p>
              <div class="flex gap-4">
                <a 
                  v-if="contactData?.github"
                  :href="contactData.github"
                  target="_blank"
                  class="text-accent hover:text-accent/80 font-semibold"
                >
                  GitHub
                </a>
                <a 
                  v-if="contactData?.linkedin"
                  :href="contactData.linkedin"
                  target="_blank"
                  class="text-accent hover:text-accent/80 font-semibold"
                >
                  LinkedIn
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

// Icons
const MailIcon = {
  template: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>'
}

const PhoneIcon = {
  template: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>'
}

const LocationIcon = {
  template: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>'
}

const GithubIcon = {
  template: '<svg fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>'
}

const LinkedInIcon = {
  template: '<svg fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'
}

// Fetch contact data
const { data: contactData } = await useAsyncData('contact', () => useApi().getContact())

const contactItems = computed(() => {
  const items = []
  
  // Only add email if it exists
  if (contactData.value?.email) {
    items.push({
      type: 'email',
      label: 'Email',
      value: contactData.value.email,
      href: `mailto:${contactData.value.email}`,
      icon: MailIcon,
      external: false
    })
  }
  
  // Add availability status
  if (contactData.value?.availability) {
    items.push({
      type: 'availability',
      label: 'Availability',
      value: contactData.value.availability,
      href: '#',
      icon: LocationIcon,
      external: false
    })
  }
  
  return items
})

const getSocialIcon = (platform: string) => {
  const icons: Record<string, any> = {
    github: GithubIcon,
    linkedin: LinkedInIcon
  }
  return icons[platform.toLowerCase()] || GithubIcon
}

onMounted(() => {
  // Animate contact items
  gsap.from('.contact-item', {
    scrollTrigger: {
      trigger: '#contact',
      start: 'top 80%'
    },
    x: -30,
    opacity: 0,
    duration: 0.8,
    stagger: 0.2
  })
  
  // Animate social links
  gsap.from('.pt-8 a', {
    scrollTrigger: {
      trigger: '.pt-8',
      start: 'top 90%'
    },
    scale: 0.9,
    opacity: 0,
    duration: 0.6,
    stagger: 0.15,
    ease: 'power3.out'
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

.social-link {
  @apply w-10 h-10 bg-secondary rounded-lg flex items-center justify-center text-text-secondary hover:text-accent hover:bg-accent/20 transition-all duration-300;
}

.pt-8 .flex a {
  opacity: 1 !important;
}
</style>