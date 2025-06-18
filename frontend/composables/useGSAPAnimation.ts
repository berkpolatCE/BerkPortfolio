export const useGSAPAnimation = () => {
  const animateOnScroll = (selector: string, options: any = {}) => {
    // Only run animations on client side
    if (!process.client) return
    
    // Use requestAnimationFrame to ensure DOM is ready
    requestAnimationFrame(() => {
      const elements = document.querySelectorAll(selector)
      if (elements.length === 0) {
        console.warn(`[GSAP] No elements found for selector: ${selector}`)
        return
      }
      
      import('gsap').then(({ gsap }) => {
        import('gsap/ScrollTrigger').then(({ ScrollTrigger }) => {
          gsap.registerPlugin(ScrollTrigger)
          
          const defaultOptions = {
            scrollTrigger: {
              trigger: elements[0],
              start: 'top 80%',
              once: true,
              markers: false
            },
            y: 50,
            opacity: 0,
            duration: 0.8,
            stagger: 0.2,
            ...options
          }
          
          gsap.from(elements, defaultOptions)
        })
      })
    })
  }
  
  const animateElement = (element: Element | null, options: any = {}) => {
    if (!process.client || !element) return
    
    import('gsap').then(({ gsap }) => {
      const defaultOptions = {
        y: 30,
        opacity: 0,
        duration: 1,
        ...options
      }
      
      gsap.from(element, defaultOptions)
    })
  }
  
  return {
    animateOnScroll,
    animateElement
  }
}