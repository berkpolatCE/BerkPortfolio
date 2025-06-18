<template>
  <div>
    <!-- SVG Noise Filter -->
    <svg class="fixed w-0 h-0">
      <defs>
        <filter id="noise">
          <feTurbulence baseFrequency="0.9" numOctaves="4" seed="5" />
          <feColorMatrix type="saturate" values="0" />
          <feComponentTransfer>
            <feFuncA type="discrete" tableValues="0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1" />
          </feComponentTransfer>
          <feGaussianBlur stdDeviation="0.5" />
        </filter>
      </defs>
    </svg>
    
    <Navigation />
    <main>
      <slot />
    </main>
  </div>
</template>