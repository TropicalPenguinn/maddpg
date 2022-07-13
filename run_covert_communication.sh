python train.py --scenario simple_crypto --good-policy ddpg --adv-policy maddpg --num-units 64 --exp-name simple_crypto_dm
python train.py --scenario simple_crypto --good-policy ddpg --adv-policy maddpg --num-units 64 --exp-name simple_crypto_dm1
python train.py --scenario simple_crypto --good-policy ddpg --adv-policy maddpg --num-units 64 --exp-name simple_crypto_dm2

python train.py --scenario simple_crypto --good-policy ddpg --adv-policy maddpg --num-units 64 --exp-name simple_crypto_dm --benchmark true
python train.py --scenario simple_crypto --good-policy ddpg --adv-policy maddpg --num-units 64 --exp-name simple_crypto_dm1 --benchmark true
python train.py --scenario simple_crypto --good-policy ddpg --adv-policy maddpg --num-units 64 --exp-name simple_crypto_dm2 --benchmark true
