const platformRouter = {
  route: null,
  name: null,
  title: '平台管理',
  type: 'folder', // 类型: folder, tab, view
  icon: 'iconfont icon-quan',
  filePath: 'views/platform/', // 文件路径
  order: null,
  inNav: true,
  children: [
    {
      title: '平台列表',
      type: 'view',
      name: 'platformList',
      route: '/platform/list',
      filePath: 'views/platform/PlatformList.vue',
      inNav: true,
      icon: 'iconfont icon-platformguanli',
    },

  ],

}

export default platformRouter
