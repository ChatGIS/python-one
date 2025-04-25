import { defineConfig } from 'vitepress'
import {f} from "vitepress/dist/node/chunk-DMuPggCS.js";

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
      { text: 'Python入门', link: '/articles/0101' }
    ],

    sidebar: [
      {
        text: 'Python入门教程',
        items: [
          { text: '你好, Python', link: '/articles/0101' },
          {
            text: 'Python基础', 
            collapsed: true,
            items: [{
              text: '注释、标识符、关键字', link: '/articles/0201'
            }, {
              text: '变量', link: '/articles/0202'
            }, {
              text: '代码缩进', link: '/articles/0203'
            }, {
              text: '基本数据类型', link: '/articles/0204'
            }, {
              text: '高级数据类型', link: '/articles/0205'
            }, {
              text: '运算符', link: '/articles/0206'
            }, {
              text: '流程控制', link: '/articles/0207'
            }] 
          },
          {
            text: '面向对象',
            collapsed: false,
            items: [
              {
                text: '理解面向对象', link: '/articles/03/01'
              },
              {
                text: '抽象性', link: '/articles/03/02'
              },
              {
                text: '函数', link: '/articles/03/03'
              },{
                text: '面向对象', link: '/articles/03/04'
              }
            ]
          },
          {
            text: '异常处理',
            collapsed: false,
            items: [
              {
                text: '常见异常', link: '/articles/04/01'
              },
              {
                text: '堆栈跟踪traceback', link: '/articles/04/02'
              },
              {
                text: '异常处理try/except', link: '/articles/04/03'
              },
              {
                text: '资源管理with/as', link: '/articles/04/04'
              }
            ]

          },
          {
            text: '文件访问',
            collapsed: false,
            items: [
              {
                text: '文件概述', link: '/articles/05/01'
              },
              {
                text: '文件函数', link: '/articles/05/02'
              },
              {
                text: '访问模式', link: '/articles/05/03'
              }
            ]
          },
          {
            text: 'GUI',
            collapsed: true,
            items: [
              {
                text: '选型', link: '/articles/0501'
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
