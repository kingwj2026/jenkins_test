const ProductLineRouter = {
  route: null,
  name: null,
  title: '产品线管理',
  type: 'folder', // 类型: folder, tab, view
  icon: 'iconfont icon-quan',
  filePath: 'views/product_line', // 文件路径
  order: null,
  inNav: true,
  children: [
        {
          title: '产品线列表',
          type: 'view',
          name: 'ProductLineList',
          route: '/product_line/list',
          filePath: 'views/product_line/ProductLineList.vue',
          inNav: true,
          icon: 'iconfont icon-product_lineguanli',
        },
      ],
}
export default ProductLineRouter
