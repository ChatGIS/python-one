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
      { text: '开始学习吧', link: '/articles/01/01' }
    ],

    sidebar: [
      {
        text: 'Python入门教程',
        items: [
          {
            text: '你好, Python',
            collapsed: true,
            items: [
              {
                text: '遥遥领先', link: '/articles/01/01'
              },
              {
                text: '关于Python', link: '/articles/01/02'
              }
            ]
          },
          {
            text: 'Python基础', 
            collapsed: true,
            items: [{
              text: '注释、标识符、关键字', link: '/articles/02/01'
            }, {
              text: '变量', link: '/articles/02/02'
            }, {
              text: '代码缩进', link: '/articles/02/03'
            }, {
              text: '基本数据类型', link: '/articles/02/04'
            }, {
              text: '高级数据类型', link: '/articles/02/05'
            }, {
              text: '运算符', link: '/articles/02/06'
            }, {
              text: '流程控制', link: '/articles/02/07'
            }] 
          },{
            text: '函数',
            collapsed: true,
            items: [
              {
                text: '函数基础', link: '/articles/03/01'
              }, {
                text: '匿名函数', link: '/articles/03/02'
              }, {
                text: '高阶函数', link: '/articles/03/03'
              }
            ]
          },
          {
            text: '面向对象',
            collapsed: true,
            items: [
              {
                text: '理解面向对象', link: '/articles/04/01'
              },
              {
                text: '抽象性', link: '/articles/04/02'
              },
              {
                text: '封装性', link: '/articles/04/03'
              },
              {
                text: '继承性', link: '/articles/04/04'
              },
              {
                text: '多态性', link: '/articles/04/05'
              }
            ]
          },
          {
            text: '异常处理',
            collapsed: true,
            items: [
              {
                text: '常见异常', link: '/articles/05/01'
              },
              {
                text: '堆栈跟踪traceback', link: '/articles/05/02'
              },
              {
                text: '异常处理try/except', link: '/articles/05/03'
              },
              {
                text: '资源管理with/as', link: '/articles/05/04'
              }
            ]

          },
          {
            text: '文件访问',
            collapsed: true,
            items: [
              {
                text: '文件概述', link: '/articles/06/01'
              },
              {
                text: '文件函数', link: '/articles/06/02'
              },
              {
                text: '访问模式', link: '/articles/06/03'
              }
            ]
          }, {
            text: '模块与包',
            collapsed: true,
            items: [
              {
                text: '模块', link: '/articles/07/01'
              }, {
                text: '包', link: '/articles/07/02'
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
