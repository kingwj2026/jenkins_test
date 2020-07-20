<template>
  <div>
    <!-- 列表页面 -->
    <div class="container" v-if="!showEdit">
      <div class="header"><div class="title">账户列表</div></div>
      <el-select v-model="form.platform_id" placeholder="请选择平台">
        <el-option
          v-for="item in Data"
          :key="item.rec_id"
          :label="item.platform_name"
          :value="item.rec_id">
          <span>{{ item.platform_name }}</span>
          <span style="float: right; color: #8492a6; font-size: 13px">{{ item.rec_id }}</span>
        </el-option>
      </el-select>
      <el-row :gutter="6">
         <el-col :span="6" ><el-input :span="6" type="text" v-model="form.user_account" placeholder="账户名"></el-input></el-col>
         <el-col :span="6" ><el-input :span="6" type="text" v-model="form.remark" placeholder="备注模糊搜索"></el-input></el-col>
         <el-col :span="6" ><el-button :span="6" type="primary"  size="biggest" @click="getPlatformUsers()">搜索</el-button></el-col><br><br>
      <el-button class="demo" type="primary" icon="el-icon-plus" size="small" @click="handleclick()">添加账户</el-button>
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
        @handleDelete="handleDelete"
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
     <DiogEdit @editClose="editClose" :EditPlatformuserId="EditPlatformuserId"></DiogEdit>
     </el-dialog><br><br>

  </div>
</template>

<script>
import LinTable from '@/components/base/table/lin-table'
import PlatformUserEdit from './PlatformUserEdit'
import DiogAdd from './PlatformUserAdd.vue';
import DiogEdit from './PlatformUserEdit.vue';
export default {
  components: {
    LinTable,
    PlatformUserEdit,
    DiogAdd,
    DiogEdit,
  },
  data() {
    return {
      tableColumn: [{ prop: 'platform_id', label: '平台号' }, { prop: 'user_account', label: '账号' }, { prop: 'phone_number', label: '手机号' }, { prop: 'email', label: '邮箱' }, { prop: 'remark', label: '备注' }],
      tableData: [],
      refreshPagination: true,  // 页数增加的时候，因为缓存的缘故，需要刷新Pagination组件
      form: {
        counts: '10',
        pages: '1',
        platform_id: '',
        user_account: '',
        remark: '',
      },
      Data: [],
      count: 0,
      operate: [],
      showEdit: false,
      openAdd: false,
      openEdit: false,
      EditPlatformuserId: 1,
    }
  },
  async created() {
    this.loading = true
    await this.getPlatformUser(this.form)
    this.operate = [
      { name: '编辑', func: 'handleEdit', type: 'primary' },
      {
        name: '删除',
        func: 'handleDelete',
        type: 'danger',
        auth: '删除账户',
      },
    ]
    this.loading = false
  },
  methods: {
    async getPlatformUser(params) {
        const platforms = await this.PUBLIC.httpRequest('cms/platform_user/get_all', params, res => {
        this.tableData = res.data
        this.count = res.count
        this.Data = res.data_platform_id
        console.log(this.tableData)
      })
      console.log(platforms)
    },
    handleEdit(val) {
      this.EditPlatformuserId = val.row.rec_id
      this.openEdit = true;//默认页面不显示为false,点击按钮将这个属性变成true
    },
    handleDelete(val) {
      this.$confirm('此操作将永久删除该账户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(async () => {
        const res = await this.PUBLIC.httpRequest('cms/platform_user/remove', { rec_id: val.row.rec_id }, data => {
             this.$message.success("删除成功")
             this.getPlatformUser(this.form)
          })
      })
    },
    async handleCurrentChange(currentPage) {
      this.form.pages = currentPage
      this.getPlatformUser(this.form)
    },
    async handleSizeChange(size) {
      this.form.counts = size
      this.getPlatformUser(this.form)
    },
    async getPlatformUsers() {
      this.form.pages = 1
      this.getPlatformUser(this.form)
    },
    handleclick(){
    this.openAdd=true;
    },
    rowClick() {},
    editClose() {
      this.openAdd = false
      this.openEdit = false
      this.getPlatformUser(this.form)
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
