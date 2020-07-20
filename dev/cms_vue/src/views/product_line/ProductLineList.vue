<template>
  <div>
    <!-- 列表页面 -->
    <div class="container" v-if="!showEdit">
      <div class="header"><div class="title">产品线列表</div></div>
      <el-select v-model="form.system_no" placeholder="请选择产品线">
        <el-option
          v-for="item in Data"
          :key="item.system_no"
          :label="item.system_name"
          :value="item.system_no">
          <span>{{ item.system_name }}</span>
          <span style="float: right; color: #8492a6; font-size: 13px">{{ item.system_no }}</span>
        </el-option>ProductLine
      </el-select>
      <el-row :gutter="6">
         <el-col :span="6" ><el-input :span="6" type="text" v-model="form.remark" placeholder="备注模糊搜索"></el-input></el-col>
         <el-col :span="6" ><el-button :span="6" type="primary"  size="biggest" @click="getProductLines()">搜索</el-button></el-col><br><br>
      <el-button class="demo" type="primary" icon="el-icon-plus" size="small" @click="handleclick()">添加产品线</el-button>
      <el-dialog  :visible.sync="openAdd" center :append-to-body='true' :lock-scroll="false" width="50%">
      <DiogAdd @editClose="editClose" ></DiogAdd>
      </el-dialog><br><br>
     </el-row>
      <!-- 表格 -->
      <lin-table
        :tableColumn="tableColumn"
        :tableData="tableData"
        :operate="operate"
        @handleEdit="handleEdit"
        @row-click="rowClick"
        v-loading="loading"
      ></lin-table>

     <!-- 分页 -->
     <div class="pagination">
        <el-pagination
           small
           @size-change="handleSizeChange"
           @current-change="handleCurrentChange"
           :background="true"
           :currentPage="form.pages"
           v-if="refreshPagination"
           :page-sizes="[5, 10, 15]"
           layout="total, sizes, prev, pager, next, jumper"
           :total="count">
        >
        </el-pagination>
    </div>

    </div>
    <!-- 编辑页面 -->
     <el-dialog :visible.sync="openEdit" center :append-to-body='true' :lock-scroll="false" width="50%">
     <DiogEdit @editClose="editClose" :EditProductLineId="EditProductLineId"></DiogEdit>
     </el-dialog><br><br>

  </div>
</template>

<script>
import LinTable from '@/components/base/table/lin-table'
import ProductLineEdit from './ProductLineEdit'
import DiogAdd from './ProductLineAdd.vue';
import DiogEdit from './ProductLineEdit.vue';
export default {
  components: {
    LinTable,
    ProductLineEdit,
    DiogAdd,
    DiogEdit,
  },
  data() {
    return {
      tableColumn: [{ prop: 'system_no', label: '产品线编号' }, { prop: 'system_name', label: '产品线名称' }, { prop: 'principal_user', label: '产品线负责人' }, { prop: 'principal_team', label: '产品线负责团队' }, { prop: 'is_disable', label: '是否停用' }, { prop: 'remark', label: '备注' }],
      tableData: [],
      refreshPagination: true,  // 页数增加的时候，因为缓存的缘故，需要刷新Pagination组件
      form: {
        counts: '10',
        pages: '1',
        system_no: '',
        remark: '',
      },
      Data: [],
      count: 0,
      operate: [],
      showEdit: false,
      openAdd: false,
      openEdit: false,
      EditProductLineId: 1,
    }
  },
  async created() {
    this.loading = true
    await this.ProductLine(this.form)
    this.operate = [
      { name: '编辑', func: 'handleEdit', type: 'primary' },
    ]
    this.loading = false
  },
  methods: {
    async ProductLine(params) {
        const platforms = await this.PUBLIC.httpRequest('cms/product_line/get_all', params, res => {
        this.tableData = res.data
        this.count = res.count
        this.Data = res.data_system_no
        console.log(this.tableData)
      })
      console.log(platforms)
    },
    handleEdit(val) {
      this.EditProductLineId = val.row.rec_id
      this.openEdit = true;//默认页面不显示为false,点击按钮将这个属性变成true
    },
    async handleCurrentChange(currentPage) {
      this.form.pages = currentPage
      this.getProductLine(this.form)
    },
    async handleSizeChange(size) {
      this.form.counts = size
      this.getProductLine(this.form)
    },
    async getProductLines() {
      this.form.pages = 1
      this.getProductLine(this.form)
    },
    handleclick(){
    this.openAdd=true;
    },
    rowClick() {},
    editClose() {
      this.openAdd = false
      this.openEdit = false
      this.getProductLine(this.form)
    },
  },
}

</script>

<style lang="scss" scoped>
.container {
  padding: 0 30px;

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    .title {
      height: 59px;
      line-height: 59px;
      color: $parent-title-color;
      font-size: 16px;
      font-weight: 500;
    }
  }

  .pagination {
    display: flex;
    justify-content: flex-end;
    margin: 20px;
    left: 80px;
  }
}

.demo {
position: absolute;
right: 40px;
top: 2px;
width: 90px;
height: 30px;
}
.choice {
position: absolute;
right: 1000px;
top: 2px;
width: 90px;
height: 30px;
}
</style>
