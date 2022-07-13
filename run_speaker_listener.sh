python train.py --scenario simple_speaker_listener --good-policy maddpg --adv-policy maddpg --num-units 64 --exp-name simple_speaker_listener_mm
python train.py --scenario simple_speaker_listener --good-policy maddpg --adv-policy maddpg --num-units 64 --exp-name simple_speaker_listener_mm1
python train.py --scenario simple_speaker_listener --good-policy maddpg --adv-policy maddpg --num-units 64 --exp-name simple_speaker_listener_mm2
python train.py --scenario simple_speaker_listener --good-policy ddpg --adv-policy ddpg --num-units 64 --exp-name simple_speaker_listener_dd
python train.py --scenario simple_speaker_listener --good-policy ddpg --adv-policy ddpg --num-units 64 --exp-name simple_speaker_listener_dd1
python train.py --scenario simple_speaker_listener --good-policy ddpg --adv-policy ddpg --num-units 64 --exp-name simple_speaker_listener_dd2

python train.py --scenario simple_speaker_listener --good-policy maddpg --adv-policy maddpg --num-units 64 --exp-name simple_speaker_listener_mm --benchmark true
python train.py --scenario simple_speaker_listener --good-policy maddpg --adv-policy maddpg --num-units 64 --exp-name simple_speaker_listener_mm1 --benchmark true
python train.py --scenario simple_speaker_listener --good-policy maddpg --adv-policy maddpg --num-units 64 --exp-name simple_speaker_listener_mm2 --benchmark true
python train.py --scenario simple_speaker_listener --good-policy ddpg --adv-policy ddpg --num-units 64 --exp-name simple_speaker_listener_dd --benchmark true
python train.py --scenario simple_speaker_listener --good-policy ddpg --adv-policy ddpg --num-units 64 --exp-name simple_speaker_listener_dd1 --benchmark true
python train.py --scenario simple_speaker_listener --good-policy ddpg --adv-policy ddpg --num-units 64 --exp-name simple_speaker_listener_dd2 --benchmark true
