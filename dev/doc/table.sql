# 平台表
DROP TABLE IF EXISTS `sys_platform`;
CREATE TABLE IF NOT EXISTS `sys_platform` (
    `rec_id`        int(11)     NOT NULL AUTO_INCREMENT,
    `platform_name` varchar(40) NOT NULL,
    `is_disable`    tinyint(1) NOT NULL DEFAULT '0',
    `remark`        varchar(255) NOT NULL DEFAULT '' COMMENT '备注',
    `create_time`   timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `update_time`   timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `delete_time`   timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`rec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='平台表';

# 平台账号表
DROP TABLE IF EXISTS `sys_platform_account`;
CREATE TABLE IF NOT EXISTS `sys_platform_account` (
    `rec_id` int(11) NOT NULL AUTO_INCREMENT,
    `platform_id`  int                                    not null,
    `user_account` varchar(40)  default ''                not null,
    `user_passwd`  varchar(128) default ''                not null,
    `remark`       varchar(255) default ''                not null comment '备注',
    `create_time`  timestamp    default CURRENT_TIMESTAMP not null,
    `update_time`  timestamp    default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    `delete_time`  timestamp    default CURRENT_TIMESTAMP not null,
    PRIMARY KEY (`rec_id`),
    UNIQUE KEY `IDX_GIFT_RULE_SEND` (`platform_id`,`user_account`,`delete_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='平台账户表';

# 系统设置表
DROP TABLE IF EXISTS `sys_setting`;
CREATE TABLE IF NOT EXISTS `sys_setting` (
    `set_key` char(64) NOT NULL,
    `set_value`   varchar(256) default ''                not null,
    `set_name`    varchar(40)  default ''                not null,
    `log_type`    tinyint      default 5                 not null comment '日志类型:sys_other_log中type值',
    `value_type`  tinyint      default 0                 not null comment '0数值型,1枚举型,2bool,3物流公司,4密码',
    `value_desc`  varchar(256) default ''                not null,
    `create_time` timestamp    default CURRENT_TIMESTAMP not null,
    `update_time` timestamp    default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    `delete_time` timestamp    default CURRENT_TIMESTAMP not null,
    PRIMARY KEY (`set_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='系统设置';

#产品线表
DROP TABLE IF EXISTS `sys_huice_system`;
CREATE TABLE IF NOT EXISTS `sys_huice_system` (
    `rec_id` int(11) NOT NULL AUTO_INCREMENT,
    `system_no`      varchar(40)                            not null comment '产品线编号',
    `system_name`    varchar(40)                            not null comment '产品线名称',
    `principal_user` varchar(40)                            not null comment '产品线负责人',
    `principal_team` varchar(40)                            not null comment '产品线负责团队',
    `is_disable`     tinyint(1)   default 0                 not null,
    `remark`         varchar(255) default ''                not null comment '备注',
    `create_time`    timestamp    default CURRENT_TIMESTAMP not null,
    `update_time`    timestamp    default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    `delete_time`    timestamp    default CURRENT_TIMESTAMP not null,
    PRIMARY KEY (`rec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='慧策产品线卖家账号表';

#卖家账号表
DROP TABLE IF EXISTS `sys_huice_system_sid`;
CREATE TABLE IF NOT EXISTS `sys_huice_system_sid` (
    `rec_id` int(11) NOT NULL AUTO_INCREMENT,
    `system_no`       int                                    not null comment '产品线编号',
    `sid`             varchar(40)                            not null comment '卖家账号',
    `status`          int          default 1                 not null comment '状态 1初始化中 20正常 30升级中 31升级失败 40准备迁移 100停用',
    `cost_type`       int          default 3                 not null comment '付费模式 1按单 2包年 3免费',
    `deploy_type`     int          default 1                 not null comment '部署模式：1单机部署 2主从部署 3集群部署 ',
    `deploy_position` int                                    not null comment '部署位置 单机模式，填写对应机器的ID，主从模式，填写主机ID，集群模式，填写集群ID',
    `is_disable`      tinyint(1)   default 0                 not null comment '是否停用',
    `stop_time`       varchar(40)  default '0000-00-00 00:00:00' not null comment '停用时间',
    `remark`          varchar(255) default ''                not null comment '备注',
    `version_id`      int          default 0                 not null comment '版本号，默认为0，每次修改必须加1',
    `create_time`     timestamp    default CURRENT_TIMESTAMP not null comment '卖家创建时间',
    `update_time`     timestamp    default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    `delete_time`     timestamp    default CURRENT_TIMESTAMP not null,
    PRIMARY KEY (`rec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='慧策产品线卖家账号表';

#卖家账号修改日志表
DROP TABLE IF EXISTS `sys_huice_system_sid_log`;
CREATE TABLE IF NOT EXISTS `sys_huice_system_sid_log` (
    `rec_id` int(11) NOT NULL AUTO_INCREMENT,
    `sid_id`      int                                 not null comment 'sys_huice_system_sid表主键',
    `type`        int                                 not null comment '操作类型 1创建卖家账号 2修改状态 3修改...',
    `sum_type`    int                                 not null comment '操作子类型',
    `message`     int                                 not null comment '操作日志',
    `create_time` timestamp default CURRENT_TIMESTAMP not null comment '日志创建时间',
    `update_time` timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    `delete_time` timestamp default CURRENT_TIMESTAMP not null,
    PRIMARY KEY (`rec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='卖家账号操作日志表';

#ECS机器资源机器
DROP TABLE IF EXISTS `sys_ecs_list`;
CREATE TABLE IF NOT EXISTS `sys_ecs_list` (
    `rec_id` int(11) NOT NULL AUTO_INCREMENT,
    `platform_id`      int                            not null comment '所属平台',
    `platform_no`        int                                 not null comment '操作类型 1创建卖家账号 2修改状态 3修改...',
    `platform_name`    int                                 not null comment '操作子类型',
    `message`     int                                 not null comment '操作日志',
    `create_time` timestamp default CURRENT_TIMESTAMP not null comment '日志创建时间',
    `update_time` timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    `delete_time` timestamp default CURRENT_TIMESTAMP not null,
    PRIMARY KEY (`rec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='卖家账号操作日志表';