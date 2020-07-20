const PlatformUserRouter = {
  route: null,
  name: null,
  title: '平台账户管理',
  type: 'folder', // 类型: folder, tab, view
  icon: 'iconfont icon-quan',
  filePath: 'views/platform_user', // 文件路径
  order: null,
  inNav: true,
  children: [
        {
          title: '账户列表',
          type: 'view',
          name: 'PlatformUserList',
          route: '/platform_user/list',
          filePath: 'views/platform_user/PlatformUserList.vue',
          inNav: true,
          icon: 'iconfont icon-platfrom_userguanli',
        },
      ],
}
export default PlatformUserRouter
