exp_config = {
    'env': {
        'manager': {
            'episode_num': float("inf"),
            'max_retry': 5,
            'step_timeout': None,
            'auto_reset': True,
            'reset_timeout': None,
            'retry_type': 'reset',
            'retry_waiting_time': 0.1,
            'shared_memory': True,
            'copy_on_get': True,
            'context': 'fork',
            'wait_num': float("inf"),
            'step_wait_timeout': None,
            'connect_timeout': 60,
            'reset_inplace': False,
            'cfg_type': 'SyncSubprocessEnvManagerDict',
            'type': 'subprocess'
        },
        'stop_value': 20,
        'type': 'atari',
        'import_names': ['dizoo.atari.envs.atari_env'],
        'collector_env_num': 8,
        'evaluator_env_num': 8,
        'n_evaluator_episode': 8,
        'env_id': 'Pong-v4',
        'frame_stack': 4
    },
    'policy': {
        'model': {
            'obs_shape': [4, 84, 84],
            'action_shape': 6,
            'action_space': 'discrete',
            'encoder_hidden_size_list': [64, 64, 128],
            'actor_head_hidden_size': 128,
            'critic_head_hidden_size': 128
        },
        'learn': {
            'learner': {
                'train_iterations': 1000000000,
                'dataloader': {
                    'num_workers': 0
                },
                'log_policy': True,
                'hook': {
                    'load_ckpt_before_run': '',
                    'log_show_after_iter': 100,
                    'save_ckpt_after_iter': 10000,
                    'save_ckpt_after_run': True
                },
                'cfg_type': 'BaseLearnerDict'
            },
            'multi_gpu': False,
            'epoch_per_collect': 10,
            'batch_size': 320,
            'learning_rate': 0.0003,
            'value_weight': 0.5,
            'entropy_weight': 0.001,
            'clip_ratio': 0.2,
            'adv_norm': True,
            'value_norm': True,
            'ppo_param_init': True,
            'grad_clip_type': 'clip_norm',
            'grad_clip_value': 0.5,
            'ignore_done': False,
            'update_per_collect': 1
        },
        'collect': {
            'collector': {
                'deepcopy_obs': False,
                'transform_obs': False,
                'collect_print_freq': 100,
                'cfg_type': 'SampleSerialCollectorDict',
                'type': 'sample'
            },
            'unroll_len': 1,
            'discount_factor': 0.99,
            'gae_lambda': 0.95,
            'n_sample': 3200
        },
        'eval': {
            'evaluator': {
                'eval_freq': 5000,
                'render': {
                    'render_freq': -1,
                    'mode': 'train_iter'
                },
                'cfg_type': 'InteractionSerialEvaluatorDict',
                'n_episode': 8,
                'stop_value': 20
            }
        },
        'other': {
            'replay_buffer': {
                'type': 'advanced',
                'replay_buffer_size': 4096,
                'max_use': float("inf"),
                'max_staleness': float("inf"),
                'alpha': 0.6,
                'beta': 0.4,
                'anneal_step': 100000,
                'enable_track_used_data': False,
                'deepcopy': False,
                'thruput_controller': {
                    'push_sample_rate_limit': {
                        'max': float("inf"),
                        'min': 0
                    },
                    'window_seconds': 30,
                    'sample_min_limit_ratio': 1
                },
                'monitor': {
                    'sampled_data_attr': {
                        'average_range': 5,
                        'print_freq': 200
                    },
                    'periodic_thruput': {
                        'seconds': 60
                    }
                },
                'cfg_type': 'AdvancedReplayBufferDict'
            },
            'commander': {
                'cfg_type': 'BaseSerialCommanderDict'
            }
        },
        'type': 'ppo_command',
        'cuda': True,
        'on_policy': True,
        'priority': False,
        'priority_IS_weight': False,
        'recompute_adv': True,
        'action_space': 'discrete',
        'nstep_return': False,
        'multi_agent': False,
        'transition_with_policy_data': True,
        'cfg_type': 'PPOCommandModePolicyDict'
    },
    'seed': 0,
    'exp_name': 'default_experiment'
}
