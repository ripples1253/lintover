r"""
Autogenerated by piltover's TL parser.

/--------------------------------------\
| It is advised not to edit this file, |
| unless you know what you are doing.  |
\--------------------------------------/

To generate again or to update the content of this file, run this command:
    $ python3 tools/gen_tl.py update
"""

from piltover.tl.types import (
    Basic,
    TLType,
    Int32,
    Int64,
    Int128,
    Int256,
    FlagsOf,
    Bit,
    TLType,
)


LAYER: int = -1


MAP = {
    0x05162463: {
        "_": "resPQ",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "pq": bytes,
            "server_public_key_fingerprints": list[Int64],
        },
        "is": "ResPQ",
    },
    0x83C95AEC: {
        "_": "p_q_inner_data",
        "params": {
            "pq": bytes,
            "p": bytes,
            "q": bytes,
            "nonce": Int128,
            "server_nonce": Int128,
            "new_nonce": Int256,
        },
        "is": "P_Q_inner_data",
    },
    0xA9F55F95: {
        "_": "p_q_inner_data_dc",
        "params": {
            "pq": bytes,
            "p": bytes,
            "q": bytes,
            "nonce": Int128,
            "server_nonce": Int128,
            "new_nonce": Int256,
            "dc": Int32,
        },
        "is": "P_Q_inner_data",
    },
    0x3C6A84D4: {
        "_": "p_q_inner_data_temp",
        "params": {
            "pq": bytes,
            "p": bytes,
            "q": bytes,
            "nonce": Int128,
            "server_nonce": Int128,
            "new_nonce": Int256,
            "expires_in": Int32,
        },
        "is": "P_Q_inner_data",
    },
    0x56FDDF88: {
        "_": "p_q_inner_data_temp_dc",
        "params": {
            "pq": bytes,
            "p": bytes,
            "q": bytes,
            "nonce": Int128,
            "server_nonce": Int128,
            "new_nonce": Int256,
            "dc": Int32,
            "expires_in": Int32,
        },
        "is": "P_Q_inner_data",
    },
    0x75A3F765: {
        "_": "bind_auth_key_inner",
        "params": {
            "nonce": Int64,
            "temp_auth_key_id": Int64,
            "perm_auth_key_id": Int64,
            "temp_session_id": Int64,
            "expires_at": Int32,
        },
        "is": "BindAuthKeyInner",
    },
    0x79CB045D: {
        "_": "server_DH_params_fail",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "new_nonce_hash": Int128,
        },
        "is": "Server_DH_Params",
    },
    0xD0E8075C: {
        "_": "server_DH_params_ok",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "encrypted_answer": bytes,
        },
        "is": "Server_DH_Params",
    },
    0xB5890DBA: {
        "_": "server_DH_inner_data",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "g": Int32,
            "dh_prime": bytes,
            "g_a": bytes,
            "server_time": Int32,
        },
        "is": "Server_DH_inner_data",
    },
    0x6643B654: {
        "_": "client_DH_inner_data",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "retry_id": Int64,
            "g_b": bytes,
        },
        "is": "Client_DH_Inner_Data",
    },
    0x3BCBF734: {
        "_": "dh_gen_ok",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "new_nonce_hash1": Int128,
        },
        "is": "Set_client_DH_params_answer",
    },
    0x46DC1FB9: {
        "_": "dh_gen_retry",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "new_nonce_hash2": Int128,
        },
        "is": "Set_client_DH_params_answer",
    },
    0xA69DAE02: {
        "_": "dh_gen_fail",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "new_nonce_hash3": Int128,
        },
        "is": "Set_client_DH_params_answer",
    },
    0xF660E1D4: {
        "_": "destroy_auth_key_ok",
        "is": "DestroyAuthKeyRes",
    },
    0x0A9F2259: {
        "_": "destroy_auth_key_none",
        "is": "DestroyAuthKeyRes",
    },
    0xEA109B13: {
        "_": "destroy_auth_key_fail",
        "is": "DestroyAuthKeyRes",
    },
    0x62D6B459: {
        "_": "msgs_ack",
        "params": {
            "msg_ids": list[Int64],
        },
        "is": "MsgsAck",
    },
    0xA7EFF811: {
        "_": "bad_msg_notification",
        "params": {
            "bad_msg_id": Int64,
            "bad_msg_seqno": Int32,
            "error_code": Int32,
        },
        "is": "BadMsgNotification",
    },
    0xEDAB447B: {
        "_": "bad_server_salt",
        "params": {
            "bad_msg_id": Int64,
            "bad_msg_seqno": Int32,
            "error_code": Int32,
            "new_server_salt": Int64,
        },
        "is": "BadMsgNotification",
    },
    0xDA69FB52: {
        "_": "msgs_state_req",
        "params": {
            "msg_ids": list[Int64],
        },
        "is": "MsgsStateReq",
    },
    0x04DEB57D: {
        "_": "msgs_state_info",
        "params": {
            "req_msg_id": Int64,
            "info": bytes,
        },
        "is": "MsgsStateInfo",
    },
    0x8CC0D131: {
        "_": "msgs_all_info",
        "params": {
            "msg_ids": list[Int64],
            "info": bytes,
        },
        "is": "MsgsAllInfo",
    },
    0x276D3EC6: {
        "_": "msg_detailed_info",
        "params": {
            "msg_id": Int64,
            "answer_msg_id": Int64,
            "bytes": Int32,
            "status": Int32,
        },
        "is": "MsgDetailedInfo",
    },
    0x809DB6DF: {
        "_": "msg_new_detailed_info",
        "params": {
            "answer_msg_id": Int64,
            "bytes": Int32,
            "status": Int32,
        },
        "is": "MsgDetailedInfo",
    },
    0x7D861A08: {
        "_": "msg_resend_req",
        "params": {
            "msg_ids": list[Int64],
        },
        "is": "MsgResendReq",
    },
    0x5E2AD36E: {
        "_": "rpc_answer_unknown",
        "is": "RpcDropAnswer",
    },
    0xCD78E586: {
        "_": "rpc_answer_dropped_running",
        "is": "RpcDropAnswer",
    },
    0xA43AD8B7: {
        "_": "rpc_answer_dropped",
        "params": {
            "msg_id": Int64,
            "seq_no": Int32,
            "bytes": Int32,
        },
        "is": "RpcDropAnswer",
    },
    0x0949D9DC: {
        "_": "future_salt",
        "params": {
            "valid_since": Int32,
            "valid_until": Int32,
            "salt": Int64,
        },
        "is": "FutureSalt",
    },
    0xAE500895: {
        "_": "future_salts",
        "params": {
            "req_msg_id": Int64,
            "now": Int32,
            "salts": list["future_salt"],
        },
        "is": "FutureSalts",
    },
    0x347773C5: {
        "_": "pong",
        "params": {
            "msg_id": Int64,
            "ping_id": Int64,
        },
        "is": "Pong",
    },
    0xE22045FC: {
        "_": "destroy_session_ok",
        "params": {
            "session_id": Int64,
        },
        "is": "DestroySessionRes",
    },
    0x62D350C9: {
        "_": "destroy_session_none",
        "params": {
            "session_id": Int64,
        },
        "is": "DestroySessionRes",
    },
    0x9EC20908: {
        "_": "new_session_created",
        "params": {
            "first_msg_id": Int64,
            "unique_id": Int64,
            "server_salt": Int64,
        },
        "is": "NewSession",
    },
    0x9299359F: {
        "_": "http_wait",
        "params": {
            "max_delay": Int32,
            "wait_after": Int32,
            "max_wait": Int32,
        },
        "is": "HttpWait",
    },
    0xD433AD73: {
        "_": "ipPort",
        "params": {
            "ipv4": Int32,
            "port": Int32,
        },
        "is": "IpPort",
    },
    0x37982646: {
        "_": "ipPortSecret",
        "params": {
            "ipv4": Int32,
            "port": Int32,
            "secret": bytes,
        },
        "is": "IpPort",
    },
    0x4679B65F: {
        "_": "accessPointRule",
        "params": {
            "phone_prefix_rules": bytes,
            "dc_id": Int32,
            "ips": list["IpPort"],
        },
        "is": "AccessPointRule",
    },
    0x5A592A6C: {
        "_": "help.configSimple",
        "params": {
            "date": Int32,
            "expires": Int32,
            "rules": list["AccessPointRule"],
        },
        "is": "help.ConfigSimple",
    },
    0x60469778: {
        "_": "req_pq",
        "params": {
            "nonce": Int128,
        },
        "ret": "ResPQ",
    },
    0xBE7E8EF1: {
        "_": "req_pq_multi",
        "params": {
            "nonce": Int128,
        },
        "ret": "ResPQ",
    },
    0xD712E4BE: {
        "_": "req_DH_params",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "p": bytes,
            "q": bytes,
            "public_key_fingerprint": Int64,
            "encrypted_data": bytes,
        },
        "ret": "Server_DH_Params",
    },
    0xF5045F1F: {
        "_": "set_client_DH_params",
        "params": {
            "nonce": Int128,
            "server_nonce": Int128,
            "encrypted_data": bytes,
        },
        "ret": "Set_client_DH_params_answer",
    },
    0xD1435160: {
        "_": "destroy_auth_key",
        "ret": "DestroyAuthKeyRes",
    },
    0x58E4A740: {
        "_": "rpc_drop_answer",
        "params": {
            "req_msg_id": Int64,
        },
        "ret": "RpcDropAnswer",
    },
    0xB921BD04: {
        "_": "get_future_salts",
        "params": {
            "num": Int32,
        },
        "ret": "FutureSalts",
    },
    0x7ABE77EC: {
        "_": "ping",
        "params": {
            "ping_id": Int64,
        },
        "ret": "Pong",
    },
    0xF3427B8C: {
        "_": "ping_delay_disconnect",
        "params": {
            "ping_id": Int64,
            "disconnect_delay": Int32,
        },
        "ret": "Pong",
    },
    0xE7512126: {
        "_": "destroy_session",
        "params": {
            "session_id": Int64,
        },
        "ret": "DestroySessionRes",
    },
}
