# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

python train.py --scenario simple_tag --good-policy maddpg --adv-policy maddpg --num-units 128 --exp-name simple_tag_mm --benchmark True
python train.py --scenario simple_tag --good-policy maddpg --adv-policy maddpg --num-units 128 --exp-name simple_tag_mm1
python train.py --scenario simple_tag --good-policy maddpg --adv-policy maddpg --num-units 128 --exp-name simple_tag_mm2
python train.py --scenario simple_tag --good-policy maddpg --adv-policy ddpg --num-units 128 --exp-name simple_tag_md
python train.py --scenario simple_tag --good-policy maddpg --adv-policy ddpg --num-units 128 --exp-name simple_tag_md1
python train.py --scenario simple_tag --good-policy maddpg --adv-policy ddpg --num-units 128 --exp-name simple_tag_md2
python train.py --scenario simple_tag --good-policy ddpg --adv-policy maddpg --num-units 128 --exp-name simple_tag_dm
python train.py --scenario simple_tag --good-policy ddpg --adv-policy maddpg --num-units 128 --exp-name simple_tag_dm1
python train.py --scenario simple_tag --good-policy ddpg --adv-policy maddpg --num-units 128 --exp-name simple_tag_dm2
python train.py --scenario simple_tag --good-policy ddpg --adv-policy ddpg --num-units 128 --exp-name simple_tag_dd
python train.py --scenario simple_tag --good-policy ddpg --adv-policy ddpg --num-units 128 --exp-name simple_tag_dd1
python train.py --scenario simple_tag --good-policy ddpg --adv-policy ddpg --num-units 128 --exp-name simple_tag_dd2
