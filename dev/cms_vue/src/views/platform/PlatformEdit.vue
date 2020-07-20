<template>
  <div class="container">
     <div class="title">修改平台信息</div>
    <div class="wrap">
      <el-row>
        <el-col :lg="16" :md="20" :sm="24" :xs="24">
          <el-form :model="form" status-icon ref="form" label-width="100px" v-loading="loading" @submit.native.prevent>
            <el-form-item label="平台ID" prop="rec_id">
              <el-input size="medium" v-model="form.rec_id" placeholder="平台ID"  :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="平台名" prop="platform_name">
              <el-input size="medium" v-model="form.platform_name" placeholder="请填写平台名"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="remark">
              <el-input size="medium" v-model="form.remark" placeholder="请填写备注"></el-input>
            </el-form-item>
            <el-form-item label="是否停用" prop="is_disable">
              <el-radio v-model="form.is_disable" :label="1">是</el-radio>
              <el-radio v-model="form.is_disable" :label="0">否</el-radio>
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
  name: 'DiogUpdate',
  props: {
    editPlatformID: {
      type: Number,
    },
  },
  data() {
    return {
      loading: false,
      form: {
        rec_id: '',
        platform_name: '',
        remark: '',
        is_disable: ''
      },
    }
  },
  async mounted() {
    console.log("111111")
    this.loading = true
    console.log(this.editPlatformID)
    await this.PUBLIC.httpRequest('cms/platform/select', { rec_id: this.editPlatformID }, data => {
      this.form = JSON.parse(data)
    })
    this.loading = false
  },

  methods: {
    async submitForm() {
      // eslint-disable-next-line no-unused-vars
      await this.PUBLIC.httpRequest('cms/platform/edit', this.form, data => {
        this.$message.success('修改成功')
        this.$emit('editClose')
      })
    },
    // 重置表单
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    back() {
      this.$emit('editClose')
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

