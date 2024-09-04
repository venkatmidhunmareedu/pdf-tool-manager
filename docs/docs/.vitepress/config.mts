import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "PTM docs",
  description: "Docs for pdf tool manager",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Docs', link: '/documentation' },
      { text: 'Downloads', link: '/downloads' },
      {
        text : 'v 0.0.1 Beta',
        items: [
          { text: 'v 0.0.1 Beta', link: '/documentation' }
        ]
      }
    ],

    search: { provider: 'local' },

    sidebar: [
      {
        text: 'Docs',
        items: [
          { text: 'Usage Guide', link: '/documentation' },
        ]
      },
      {
        text: 'Downloads',
        items: [
          { text: 'PDF Tool Manager', link: '/downloads' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/venkatmidhunmareedu/pdf-tool-manager.git' }
    ]
  }
})
