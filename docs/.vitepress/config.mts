import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "PTM docs",
  description: "Docs for pdf tool manager",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Docs', link: '/docs' },
      { text: 'Downloads', link: '/downloads' },
      { text: 'Examples', link: '/examples' },
    ],

    search: { provider: 'local' },

    sidebar: [
      {
        text: 'Docs',
        items: [
          { text: 'How to Merge?', link: '/docs/merge' },
          { text: 'How to Split?', link: '/docs/split' },
          { text: 'How to Compress?', link: '/docs/compress' },
          { text: 'How to Pdf2Images?', link: '/docs/pdf2images' },
          { text: 'How to Images2Pdf?', link: '/docs/images2pdf' },
          { text: 'How to EncryptPdf?', link: '/docs/encryptpdf' },
          { text: 'How to UnlockPdf?', link: '/docs/unlockpdf' },
          { text: 'How to RedactPdf?', link: '/docs/redactpdf' }
        ]
      },
      {
        text: 'Downloads',
        items: [
          { text: 'PDF Tool Manager', link: '/downloads' },
        ]
      },
      {
        text: 'Examples',
        items: [
          { text: 'Example for Merging PDF', link: '/examples/merge' },
          { text: 'Example for Splitting PDF', link: '/examples/split' },
          { text: 'Example for Compressing PDF', link: '/examples/compress' },
          { text: 'Example for PDF to Images', link: '/examples/pdf2images' },
          { text: 'Example for Images to PDF', link: '/examples/images2pdf' },
          { text: 'Example for Encrypting PDF', link: '/examples/encryptpdf' },
          { text: 'Example for Unlocking PDF', link: '/examples/unlockpdf' },
          { text: 'Example for Redacting PDF', link: '/examples/redactpdf' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/venkatmidhunmareedu/pdf-tool-manager.git' }
    ]
  }
})
