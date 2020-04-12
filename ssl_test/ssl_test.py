import OpenSSL
from OpenSSL import crypto


# 参考 https://blog.csdn.net/qq874455953/article/details/85041415


root_ca_file = r"cert/root_cert.pem"
server_ca_file = r"cert/server_ca.pem"
server_file = r"cert/server.pem"
ca_chain_file = r'cert/server_chain_ca.pem'


# test_cert_file = server_file
# cert_file_text = open(test_cert_file, "rb").read()
# cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_file_text)
# print(cert.get_issuer())
# print(cert.get_subject())

csdn_file = r"download_cert/csdn_net.cer"
csdn_chain_file = r"download_cert/csdn_chain.cer"

test_ca_file = csdn_chain_file
ca_file_text = open(test_ca_file, "rb").read()
ca = crypto.load_certificate(crypto.FILETYPE_PEM, ca_file_text)
print(ca.get_version())
print(ca.get_signature_algorithm())
print(ca.get_issuer().commonName)
print(ca.get_subject().commonName)