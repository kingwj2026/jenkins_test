<template>
  <div class="container">
    <div class="title">
      <span style="margin-right:300px;">编辑账户</span>
    </div>
    <el-divider></el-divider>
    <div class="wrap">
      <el-row>
        <el-col :lg="16" :md="20" :sm="24" :xs="24">
          <el-form :model="form" status-icon ref="form" label-width="100px" v-loading="loading" @submit.native.prevent>

           <el-form-item label="平台ID" prop="platform_id">
              <el-input size="medium" v-model="form.platform_id" disabled placeholder="请填写平台id"></el-input>
            </el-form-item>

            <el-form-item label="账户名" prop="user_account">
              <el-input size="medium" v-model="form.user_account" placeholder="请填写账户名"></el-input>
            </el-form-item>

            <el-form-item label="密码" prop="user_passwd">
              <el-input size="medium" v-model="form.user_passwd" placeholder="新密码"></el-input>
            </el-form-item>

            <el-form-item label="手机号" prop="phone_number">
              <el-input size="medium" v-model="form.phone_number" placeholder="新手机号"></el-input>
            </el-form-item>

            <el-form-item label="邮箱" prop="email">
              <el-input size="medium" v-model="form.email" placeholder="新邮箱"></el-input>
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
  name: 'DiogEdit',
  props: {
    EditPlatformuserId: {
      type: Number,
    },
  },
  data() {
    return {
      loading: false,
      form: {
        platform_id: '',
        user_account: '',
        user_passwd: '',
        phone_number: '',
        email: '',
        remark: ''
      },
    }
  },

  async mounted() {
    this.loading = true
    console.log(this.EditPlatformuserId)
    await this.PUBLIC.httpRequest('cms/platform_user/select', { rec_id: this.EditPlatformuserId }, data => {
      this.form = JSON.parse(data)
      })
    this.loading = false
  },

  methods: {
    async submitForm() {
        await this.PUBLIC.httpRequest('cms/platform_user/edit', this.form, data => {
        this.$message.success('修改成功')
        this.$emit('editClose')
        resetForm(formName)
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
.el-divider--horizontal {
  margin: 0;
}
.container {
  .title {
    height: 59px;
    line-height: 59px;
    color: $parent-title-color;
    font-size: 16px;
    font-weight: 500;
    text-indent: 40px;
    .back {
      float: right;
      margin-right: 40px;
      cursor: pointer;
    }
  }
  .wrap {
    padding: 20px;
  }
  .submit {
    float: left;
  }
}
