<template>
  <div class="container">
    <div class="title">
      <span style="margin-right:300px;">编辑产品线</span>
    </div>
    <el-divider></el-divider>
    <div class="wrap">
      <el-row>
        <el-col :lg="16" :md="20" :sm="24" :xs="24">
          <el-form :model="form" status-icon ref="form" label-width="100px" v-loading="loading" @submit.native.prevent>

           <el-form-item label="平台ID" prop="system_no">
              <el-input size="medium" v-model="form.system_no" disabled placeholder="请填写产品线编号"></el-input>
            </el-form-item>

            <el-form-item label="账户名" prop="system_name">
              <el-input size="medium" v-model="form.system_name" placeholder="请填写产品线名称"></el-input>
            </el-form-item>

            <el-form-item label="密码" prop="principal_user">
              <el-input size="medium" v-model="form.principal_user" placeholder="产品线负责人"></el-input>
            </el-form-item>

            <el-form-item label="手机号" prop="principal_team">
              <el-input size="medium" v-model="form.principal_team" placeholder="产品线负责团队"></el-input>
            </el-form-item>

            <el-form-item label="邮箱" prop="is_disable">
              <el-input size="medium" v-model="form.is_disable" placeholder="是否停用"></el-input>
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
    EditProductLineId: {
      type: Number,
    },
  },
  data() {
    return {
      loading: false,
      form: {
        system_no: '',
        system_name: '',
        principal_user: '',
        principal_team: '',
        is_disable: '',
        remark: ''
      },
    }
  },

  async mounted() {
    this.loading = true
    console.log(this.EditProductLineId)
    await this.PUBLIC.httpRequest('cms/product_line/select', { rec_id: EditProductLineId }, data => {
      this.form = JSON.parse(data)
      })
    this.loading = false
  },

  methods: {
    async submitForm() {
        await this.PUBLIC.httpRequest('cms/product_line/edit', this.form, data => {
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
