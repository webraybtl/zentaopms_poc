# 禅道系统权限绕过到命令执行


## 漏洞概述

禅道是第一款国产的开源项目管理软件，它的核心管理思想基于敏捷方法 scrum，内置了产品管理和项目管理，同时又根据国内研发现状补充了测试管理、计划管理、发布管理、文档管理、事务管理等功能，在一个软件中就可以将软件研发中的需求、任务、bug、用例、计划、发布等要素有序地跟踪管理起来，完整地覆盖了项目管理的核心流程。
该漏洞是由于禅道项目管理系统权限认证存在缺陷导致，攻击者可利用该漏洞在未授权的情况下，通过权限绕过在服务器执行任意命令。

## 影响范围

|  禅道系统   | 影响版本  |
|  ----  | ----  |
| 开源版  | 17.4以下的未知版本<=version<=18.0.beta1 |
| 旗舰版  | 3.4以下的未知版本<=version<=4.0.beta1 |
| 企业版  | 7.4以下的未知版本<=version<=8.0.beta1 8.0.beta2 |

## 详情分析
![blockchain](https://github.com/webraybtl/zentaopms_poc/blob/main/1673535459685.jpg "公众号")


查看分析文章[https://mp.weixin.qq.com/s/ZHsYaU31WkzAJijy1V0U1w](https://mp.weixin.qq.com/s/ZHsYaU31WkzAJijy1V0U1w)

## 免责声明:

本篇文章仅用于技术交流学习和研究的目的，严禁使用文章中的技术用于非法目的和破坏，否则造成一切后果与发表本文章的作者无关。

### 中文版本:

本免责声明旨在明确指出，本文仅为技术交流、学习和研究之用，不得将文章中的技术用于任何非法目的或破坏行为。发表本文章的作者对于任何非法使用技术或对他人或系统造成的损害概不负责。

阅读和参考本文章时，您必须明确并承诺，不会利用文章中提供的技术来实施非法活动、侵犯他人的权益或对系统进行攻击。任何使用本文中的技术所导致的任何意外、损失或损害，包括但不限于数据损失、财产损失、法律责任等问题，都与发表本文章的作者无关。

本文提供的技术信息仅供学习和参考之用，不构成任何形式的担保或保证。发表本文章的作者不对技术的准确性、有效性或适用性做任何声明或保证。

### 英文版本:

This disclaimer is intended to clearly state that this article is solely for the purpose of technical exchange, learning, and research, and the use of the techniques mentioned in the article for any illegal purposes or destructive actions is strictly prohibited. The author of this article shall not be held responsible for any consequences resulting from the misuse of the techniques mentioned.

By reading and referring to this article, you must acknowledge and commit that you will not exploit the techniques provided in the article for any illegal activities, infringement of rights of others, or attacks on systems. The author of this article bears no responsibility for any accidents, losses, or damages caused by the use of the techniques mentioned in this article, including but not limited to data loss, property damage, legal liabilities, etc.

The technical information provided in this article is for learning and reference purposes only and does not constitute any form of warranty or guarantee. The author of this article makes no representations or warranties regarding the accuracy, effectiveness, or applicability of the techniques mentioned.

