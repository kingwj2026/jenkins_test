<template>
  <div class="container">
    <div class="title" >新建产品线</div>
    <div class="wrap">
      <el-row>
        <el-col :lg="16" :md="20" :sm="24" :xs="24">
          <el-form :model="form" status-icon ref="form" label-width="100px" @submit.native.prevent>

            <el-form-item label="产品线编号" prop="system_no">
              <el-input size="medium" v-model="form.system_no" placeholder="请填写产品线编号"></el-input>
            </el-form-item>

            <el-form-item label="产品线名称" prop="system_name">
              <el-input size="medium" v-model="form.system_name" placeholder="请填写产品线名称"></el-input>
            </el-form-item>

            <el-form-item label="负责人" prop="principal_user">
              <el-input size="medium" v-model="form.principal_user" placeholder="请填写产品线负责人"></el-input>
            </el-form-item>

            <el-form-item label="负责团队" prop="principal_team">
              <el-input size="medium" v-model="form.principal_team" placeholder="请填写产品线负责团队"></el-input>
            </el-form-item>

            <el-form-item label="是否停用" prop="is_disable">
              <el-input size="medium" v-model="form.is_disable" placeholder="请填写是否停用"></el-input>
            </el-form-item>

            <el-form-item label="备注" prop="remark">
              <el-input size="medium" v-model="form.remark" placeholder="请填写备注"></el-input>
            </el-form-item>

            <el-form-item class="submit">
              <el-button type="primary" @click="submitForm('form')">保 存</el-button>
              <el-button @click="resetForm('form')">重 置</el-button>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
    </div>
  </div>
</template>


<script>

export default {
  name: 'DiogAdd',
  data() {
    return {
      form: {
        rec_id: '',
        system_no: '',
        system_name: '',
        principal_user: '',
        principal_team: '',
        is_disable: '',
        remark: '',
      },
    }
  },

  methods: {
    async submitForm(formName) {
        await this.PUBLIC.httpRequest('cms/product_line/create', this.form, data => {
        this.$message.success('新建账户成功')
        this.$emit('editClose')
      })
    },
    // 重置表单
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  .title {
    height: 59px;
    line-height: 59px;
    color: $parent-title-color;
    font-size: 16px;
    font-weight: 500;
    text-indent: 40px;
    border-bottom: 1px solid #dae1ec;
  }
  .wrap {
    padding: 20px;
  }
  .submit {
    float: left;
  }
}
</style>
