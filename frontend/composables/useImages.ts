export const useImages = () => {
  // Map project IDs to local image paths
  const projectImages: Record<number, string> = {
    1: '/images/project1.jpg',
    2: '/images/project2.jpg',
  }

  // Profile image
  const profileImage = '/images/profile.jpg'

  // Get project image by ID with fallback
  const getProjectImage = (projectId: number): string | null => {
    return projectImages[projectId] || null
  }

  // Get profile image
  const getProfileImage = (): string => {
    return profileImage
  }

  return {
    projectImages,
    profileImage,
    getProjectImage,
    getProfileImage
  }
}