<template>
  <div>
    <!-- 列表页面 -->
    <div class="container">
      <div class="header"><div class="title">配置列表</div></div>
         <el-dialog  :visible.sync="openOff" center :append-to-body='true' :lock-scroll="false" width="50%">
            <Diog @editClose="editClose"></Diog>
         </el-dialog>
         <el-row :gutter="20">
             <el-col :span="6" ><el-input type="text" v-model="inputform.set_key" placeholder="配置项key"></el-input></el-col>
             <el-col :span="6" ><el-input type="text" v-model="inputform.set_name" placeholder="配置名称"></el-input></el-col>
             <el-col :span="6" ><el-input type="text" v-model="inputform.value_desc" placeholder="配置值说明"></el-input></el-col>
             <el-col :span="2" ><el-button  type="primary"  size="big" @click="get_sys_settings(inputform)">搜索</el-button></el-col>
             <el-col :span="4" ><el-button type="primary" icon="el-icon-plus" size="big" @click="handleclick()">添加系统配置项</el-button></el-col><br><br>
         </el-row>
         <!-- 表格 -->
         <lin-table
            :tableData="tableData"
            :tableColumn="tableColumn"
            :operate="operate"
            @handleEdit="handleEdit"
            @handleDelete="handleDelete"
            @row-click="rowClick"
            v-loading="loading"
          ></lin-table>
         <el-pagination class="pagination"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :currentPage=inputform.pages
            :page-sizes="[5, 10, 20, 40]"
            :pageSize=inputform.counts
            layout="total, sizes, prev, pager, next, jumper"
            :total= total>
         </el-pagination>
      </div>
         <!-- 编辑弹框实现 -->
         <el-dialog :visible.sync="openUpdate" center :append-to-body='true' :lock-scroll="false" width="50%">
             <DiogUpdate @editClose="editClose" :editPlatformID="editPlatformID"></DiogUpdate>
         </el-dialog><br><br>
  </div>
</template>

<script>
import LinTable from '@/components/base/table/lin-table'
import Diog from './SysConfigAdd.vue';
import DiogUpdate from './SysConfigEdit.vue';


export default {
  components: {
    LinTable,
    Diog,
    DiogUpdate,

  },

  data() {
    return {
      tableColumn: [{ prop: 'set_key', label: '配置项key' }, { prop: 'set_value', label: '配置值' },
                    { prop: 'set_name', label: '配置名称' }, { prop: 'log_type', label: '日志类型' },
                    { prop: 'log_type', label: '配置值类型' }, { prop: 'value_desc', label: '配置说明' },
                    { prop: 'is_disable', label: '是否停用' }],
      inputform: {
        pages: 1, //初始页
        counts: 10, //    每页的数据
        set_key: '',
        set_name: '',
        value_desc: '',
      },
      tableData: [],
      operate: [],
      openOff: false,
      openUpdate: false,
      editPlatformID: 1,
      total: '',
    }
  },
  async created() {
    this.loading = true
    await this.get_sys_settings()
    this.operate = [
      { name: '编辑', func: 'handleEdit', type: 'primary' },
      {
        name: '禁用',
        func: 'handleDelete',
        type: 'danger',
        auth: '禁用平台',
      },
    ]
    this.loading = false
  },

  methods: {
    async get_sys_settings() {
       await this.PUBLIC.httpRequest(`cms/sys_setting/get_sys_settings`, this.inputform,  data => {
         this.total = data.total
         this.tableData = data.data
         for(let i in this.tableData){
            this.tableData[i].is_disable = this.transStatus(this.tableData[i].is_disable)
         }
         //this.$message.success("获取成功")
        })
     },
    // 获取所拥有的权限并渲染  由子组件提供
    handleEdit(val) {
      this.editPlatformID = val.row.set_key
      this.openUpdate = true;//默认页面不显示为false,点击按钮将这个属性变成true
    },

    //禁用系统配置
    handleDelete(val) {
      this.$confirm('此操作将禁用该系统配置项, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(async () => {
       await this.PUBLIC.httpRequest(`cms/sys_setting/disabled`,{set_key: val.row.set_key, is_disable: val.row.is_disable}, data => {
             this.$message.success("禁用成功")
             this.get_sys_settings()
             })
      })
    },
    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange(size) {
            this.get_sys_settings()
            this.inputform.counts = size;
            this.get_sys_settings()
            console.log(this.inputform.counts)  //每页下拉显示数据
    },
    handleCurrentChange(currentPage){
            this.inputform.pages = currentPage;
            //重新获取列表
            this.get_sys_settings()
            console.log(this.inputform.pages)  //点击第几页
    },
    handleclick(){
      this.openOff=true;//默认页面不显示为false,点击按钮将这个属性变成true
    },
    //关闭弹框并刷新页面
    editClose() {
      //关闭openOff组件
      this.openOff = false
      //关闭openUpdate组件
      this.openUpdate = false
      //重新获取列表
      this.get_sys_settings(this.inputform)
    },
    rowClick() {},
    transStatus(n){
       let str='';
       if(n==0){
            str='否'
       }else if(n==1){
            str='是'
      }
    return str;
   },
  }
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
 .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
   .el-input {
    border-radius: 4px;
  }
  .pagination {
    display: flex;
    justify-content: flex-end;
    margin: 20px;
  }
}
</style>
