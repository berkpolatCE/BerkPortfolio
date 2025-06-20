export const useScrollTo = () => {
  const scrollToElement = (elementId: string, offset: number = 80) => {
    // Remove the # if present
    const id = elementId.replace('#', '')
    
    // Use a more robust scroll implementation
    const performScroll = (targetPosition: number) => {
      // Cancel any existing smooth scroll behavior
      document.documentElement.style.scrollBehavior = 'auto'
      document.body.style.scrollBehavior = 'auto'
      
      // Perform the scroll
      const startPosition = window.pageYOffset
      const distance = targetPosition - startPosition
      const duration = 800 // milliseconds
      let start: number | null = null
      
      const step = (timestamp: number) => {
        if (!start) start = timestamp
        const progress = timestamp - start
        const percentage = Math.min(progress / duration, 1)
        
        // Easing function for smooth animation
        const easeInOutCubic = (t: number) => {
          return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2
        }
        
        window.scrollTo(0, startPosition + distance * easeInOutCubic(percentage))
        
        if (progress < duration) {
          requestAnimationFrame(step)
        } else {
          // Restore scroll behavior
          document.documentElement.style.scrollBehavior = ''
          document.body.style.scrollBehavior = ''
        }
      }
      
      requestAnimationFrame(step)
    }
    
    if (id === '' || id === '/') {
      // Scroll to top
      performScroll(0)
      return
    }
    
    const element = document.getElementById(id)
    if (!element) {
      console.warn(`Element with id "${id}" not found`)
      return
    }
    
    // Calculate position with offset for fixed header
    const elementPosition = element.getBoundingClientRect().top
    const offsetPosition = elementPosition + window.pageYOffset - offset
    
    performScroll(offsetPosition)
  }
  
  const handleAnchorClick = (event: Event, href: string, offset: number = 80) => {
    // Only handle anchor links
    if (href && href.includes('#')) {
      event.preventDefault()
      
      // Extract the hash part
      const hashIndex = href.indexOf('#')
      const hash = href.substring(hashIndex + 1)
      
      scrollToElement(hash, offset)
    }
  }
  
  return {
    scrollToElement,
    handleAnchorClick
  }
}