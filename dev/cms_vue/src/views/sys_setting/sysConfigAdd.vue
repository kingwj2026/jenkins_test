<template>
  <div class="container">
    <div class="title">新建配置</div>
    <div class="wrap">
      <el-row>
        <el-col :lg="16" :md="20" :sm="24" :xs="24">
          <el-form :model="form" status-icon ref="form" label-width="100px" @submit.native.prevent>
            <el-form-item label="系统配置key" prop="set_key">
              <el-input size="medium" v-model="form.set_key" placeholder="系统配置key"></el-input>
            </el-form-item>
            <el-form-item label="配置值" prop="set_value">
              <el-input size="medium" v-model="form.set_value" placeholder="请填写配置值"></el-input>
            </el-form-item>
            <el-form-item label="配置名称" prop="set_name">
              <el-input size="medium" v-model="form.set_name" placeholder="请填写配置名称"></el-input>
            </el-form-item>
            <el-form-item label="日志类型" prop="log_type">
              <el-input size="medium" v-model="form.log_type" placeholder="请选择日志类型"></el-input>
            </el-form-item>
            <el-form-item label="配置值类型" prop="value_type">
              <el-input size="medium" v-model="form.value_type" placeholder="请填写配置值类型"></el-input>
            </el-form-item>
            <el-form-item label="配置值说明" prop="value_desc">
              <el-input size="medium" v-model="form.value_desc" placeholder="请填写配置说明"></el-input>
            </el-form-item>
            <el-form-item label="是否停用" prop="is_disable">
              <el-radio v-model="form.is_disable" label="1">是</el-radio>
              <el-radio v-model="form.is_disable" label="0">否</el-radio>
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
    name: 'Diog',
    data() {
       return {
          form: {
            set_key: '',
            set_value: '',
            set_name: '',
            log_type: '',
            log_type: '',
            value_desc: '',
            is_disable: '',
          },
       }
     },
  methods: {
    async submitForm(formName) {
      await this.PUBLIC.httpRequest('cms/sys_setting/create', { info: this.form }, data => {
        this.$message.success('新建成功')
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
