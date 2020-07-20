const sysConfigRouter = {
  route: null,
  name: null,
  title: '系统配置',
  type: 'folder', // 类型: folder, tab, view
  icon: 'iconfont icon-quan',
  filePath: 'views/sysConfig/', // 文件路径
  order: null,
  inNav: true,
  children: [
    {
      title: '配置列表',
      type: 'view',
      name: 'sysConfigList',
      route: '/sysConfig/list',
      filePath: 'views/sysConfig/sysConfigList.vue',
      inNav: true,
      icon: 'iconfont icon-sysConfig',
    },
  ],

}

export default sysConfigRouter