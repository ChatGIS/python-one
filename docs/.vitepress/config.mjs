import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/python-one/',
  title: "Python One",
  head: [['link', { rel: 'icon', href: 'https://chatgis.space/images/favicon.png' }]],
  description: "One notebook of Python",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '主页', link: '/' },
      { text: 'Python入门', link: '/python/0101' }
    ],

    sidebar: [
      {
        text: 'Python入门教程',
        items: [
          { text: '你好, Python', link: '/python/0101' },
          {
            text: 'Python基础', 
            collapsed: false,
            items: [{
              text: '注释、标识符、关键字', link: '/python/0201'
            }, {
              text: '变量', link: '/python/0202'
            }, {
              text: '代码缩进', link: '/python/0203'
            }, {
              text: '基本数据类型', link: '/python/0204'
            }, {
              text: '高级数据类型', link: '/python/0205'
            }, {
              text: '运算符', link: '/python/0206'
            }, {
              text: '流程控制', link: '/python/0207'
            }] 
          },
          {
            text: '面向对象',
            collapsed: false,
            items: [
              {
                text: '函数', link: '/python/0301'
              },{
                text: '面向对象', link: '/python/0302'
              }
            ]
          },
          {
            text: '文件访问',
            collapsed: false,
            items: [
              {
                text: '文件', link: '/python/0401'
              }
            ]
          },
          {
            text: 'GUI',
            collapsed: false,
            items: [
              {
                text: '选型', link: '/python/0501'
              }
            ]
          }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/ChatGIS/python-one' }
    ]
  }
})
