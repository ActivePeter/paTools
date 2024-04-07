# wget https://github.com/vmware-tanzu/velero/releases/download/v1.13.1/velero-v1.13.1-linux-amd64.tar.gz
# tar -xzvf velero-v1.13.1-linux-amd64.tar.gz
# sudo mv velero-v1.13.1-linux-amd64/velero /usr/local/bin/

# velero install \
#   --provider aws \
#   --plugins velero/velero-plugin-for-aws:v1.2.0 \
#   --bucket your-velero-bucket \
#   --secret-file ./minio.credentials \
#   --use-volume-snapshots=false \
#   --backup-location-config region=minio,s3ForcePathStyle="true",s3Url=https://minio.example.com
import os
import yaml

CUR_FPATH = os.path.abspath(__file__)
CUR_FDIR = os.path.dirname(CUR_FPATH)

# chdir to the directory of this script
os.chdir(CUR_FDIR)

# read yaml
# 打开并读取YAML文件
with open('velero_config.yaml', 'r') as file:
    # 加载YAML数据
    data = yaml.safe_load(file)

MINIO_ID=data['minio_id']
MINIO_PW=data['minio_pw']
MINIO_BUCKET=data['minio_bucket']
MINIO_ENDPOINT=data['minio_endpoint']


with open('velero-minio-credentials', 'w') as f:
    # 写入内容到文件
    f.write(f"""
    [default]
    aws_access_key_id = {MINIO_ID}
    aws_secret_access_key = {MINIO_PW}
    """)

# # cat velero-minio-config.yaml
# # 打开文件以写入模式
# with open('velero-minio-config.yaml', 'w') as f:
#     # 写入内容到文件
#     f.write(f"""
# credentialsFile: ./velero-minio-credentials
# backupStorageLocation:
#     bucket: {MINIO_BUCKET}
#         config:
#             region: us-east-1
#             s3ForcePathStyle: "true"
#             s3Url: http://{MINIO_ENDPOINT}:9000
#         name: minio
#         provider: aws
#     """)

os.system(
"""
velero install \
    --provider aws \
    --plugins velero/velero-plugin-for-aws:v1.2.1 \
    --bucket {MINIO_BUCKET} \
    --secret-file ./velero-minio-credentials \
    --use-volume-snapshots=false \
    --backup-location-config region=minio,s3ForcePathStyle="true",s3Url=http://{MINIO_ENDPOINT}:9000 \
    --use-node-agent
"""
)

# os.system("rm -f velero-minio-config.yaml")


