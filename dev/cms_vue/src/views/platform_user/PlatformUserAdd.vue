<template>
  <div class="container">
    <div class="title" >新建账户</div>
    <div class="wrap">
      <el-row>
        <el-col :lg="16" :md="20" :sm="24" :xs="24">
          <el-form :model="form" status-icon ref="form" label-width="100px" @submit.native.prevent>

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

            <el-form-item label="账号名" prop="user_account">
              <el-input size="medium" v-model="form.user_account" placeholder="请填写账号名"></el-input>
            </el-form-item>

            <el-form-item label="密码" prop="user_passwd">
              <el-input size="medium" v-model="form.user_passwd" placeholder="请填写密码"></el-input>
            </el-form-item>

            <el-form-item label="手机号" prop="phone_number">
              <el-input size="medium" v-model="form.phone_number" placeholder="请填写手机号"></el-input>
            </el-form-item>

            <el-form-item label="邮箱" prop="email">
              <el-input size="medium" v-model="form.email" placeholder="请填写邮箱"></el-input>
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
        platform_id: '',
        user_account: '',
        user_passwd: '',
        phone_number: '',
        email: '',
        remark: '',
      },
      Data:[],
    }
  },
  async mounted() {
    this.loading = true
    await this.PUBLIC.httpRequest('cms/platform_user/get_all', { platform_id: '', user_account: '', remark: '', pages: '1', counts: '10' }, res => {
        this.Data = res.data_platform_id
    })
    this.loading = false
  },
  methods: {
    async submitForm(formName) {
        await this.PUBLIC.httpRequest('cms/platform_user/create', this.form, data => {
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
