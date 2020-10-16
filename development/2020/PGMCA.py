# DU PG MCA 2020 6th sem - 16-10-2020

# dependencies
import requests
from bs4 import BeautifulSoup
import re
import sys
import os

savePath = "html"
if not os.path.isdir(savePath):
    os.mkdir(savePath)

# link for 6th sem 2020 - new link
GradeCard = "http://rslt.duresult.in/Students/Combine_GradeCard.aspx"


CONST_VIEWSTATE = """/wEPDwUJLTUzMzY3NDA2DxYEHgdjYXB0Y2hhBQYxMTc1MDMeCUlwQWRkcmVzcwULNTIuOTUuNzUuMTAWAgIDD2QWDAIBD2QWAgIFDw8WAh4EVGV4dAU0UmVzdWx0cyAoU2VtZXN0ZXIvQW5udWFsIEV4YW1pbmF0aW9uIE1heS1KdW5lIDIwMjAgKWRkAgcPDxYCHwIFECAoTWF5LUp1bmUgMjAyMClkZAIVDxAPFgYeDURhdGFUZXh0RmllbGQFCUNPTExfTkFNRR4ORGF0YVZhbHVlRmllbGQFCUNPTExfQ09ERR4LXyFEYXRhQm91bmRnZBAVowESPC0tLS0tU2VsZWN0LS0tLS0+HEFjaGFyeWEgTmFyZW5kcmEgRGV2IENvbGxlZ2UkQWRpdGkgTWFoYXZpZGhsYXlhIChUZWFjaGluZyBDZW50cmUpE0FkaXRpIE1haGF2aWR5YWxheWEkQXJ5YWJoYXR0YSBDb2xsZWdlIChUZWFjaGluZyBDZW50cmUpPUFyeWFiaGF0dGEgQ29sbGVnZSBbRm9ybWVybHkgUmFtIExhbCBBbmFuZCBDb2xsZWdlIChFdmVuaW5nKV0fQXRtYSBSYW0gU2FuYXRhbiBEaGFyYW0gQ29sbGVnZRhCaGFnaW5pIE5pdmVkaXRhIENvbGxlZ2UqQmhhZ2luaSBOaXZlZGl0YSBDb2xsZWdlIChUZWFjaGluZyBDZW50cmUpD0JoYXJhdGkgQ29sbGVnZSFCaGFyYXRpIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUqQmhhc2thcmFjaGFyeWEgQ29sbGVnZSBvZiBBcHBsaWVkIFNjaWVuY2VzEUNBTVBVUyBMQVcgQ0VOVFJFIkNsdXN0ZXIgSW5ub3ZhdGlvbiBDZW50cmUgKEMuSS5DLikdQ29sbGVnZSBPZiBWb2NhdGlvbmFsIFN0dWRpZXMvQ29sbGVnZSBvZiBWb2NhdGlvbmFsIFN0dWRpZXMgKFRlYWNoaW5nIENlbnRyZSkSRGF1bGF0IFJhbSBDb2xsZWdlHERlZW4gRGF5YWwgVXBhZGh5YXlhIENvbGxlZ2UuRGVlbiBEYXlhbCBVcGFkaHlheWEgQ29sbGVnZSAoVGVhY2hpbmcgQ2VudHJlKSBEZWxoaSBDb2xsZWdlIE9mIEFydHMgJiBDb21tZXJjZRpEZWxoaSBTY2hvb2wgb2YgSm91cm5hbGlzbR1EZXBhcnRtZW50IG9mIEFkdWx0IEVkdWNhdGlvbh1EZXBhcnRtZW50IG9mIEFmcmljYW4gU3R1ZGllcxpEZXBhcnRtZW50IG9mIEFudGhyb3BvbG9neRREZXBhcnRtZW50IG9mIEFSQUJJQ1NEZXBhcnRtZW50IG9mIEIuQSAoUHJvZ3JhbW1lIENvbW1pdHRlZSkgQXBwbGljYXRpb24gQ291cnNlLUlJSSBGb3VuZGF0aW9uIENvdXJzZS1JSSJEZXBhcnRtZW50IG9mIEJpbyBNZWRpY2FsIFJlc2VhcmNoG0RlcGFydG1lbnQgb2YgQmlvLWNoZW1pc3RyeRREZXBhcnRtZW50IG9mIEJvdGFueR5EZXBhcnRtZW50IG9mIEJ1ZGRoaXN0IFN0dWRpZXMgRGVwYXJ0bWVudCBvZiBCdXNpbmVzcyBFY29ub21pY3MXRGVwYXJ0bWVudCBvZiBDaGVtaXN0cnkWRGVwYXJ0bWVudCBvZiBDb21tZXJjZR5EZXBhcnRtZW50IG9mIENvbXB1dGVyIFNjaWVuY2UgRGVwYXJ0bWVudCBvZiBFYXN0IEFzaWFuIFN0dWRpZXMXRGVwYXJ0bWVudCBvZiBFY29ub21pY3MgRGVwYXJ0bWVudCBvZiBFZHVjYXRpb24gKEMuSS5FLikgRGVwYXJ0bWVudCBvZiBFbGVjdHJvbmljIFNjaWVuY2UVRGVwYXJ0bWVudCBvZiBFbmdsaXNoI0RlcGFydG1lbnQgb2YgRW52aXJvbm1lbnRhbCBTdHVkaWVzPURlcGFydG1lbnQgb2YgRmFjdWx0eSBvZiBBcHBsaWVkIFNvY2lhbCBTY2llbmNlcyAmIEh1bWFuaXRpZXMgRGVwYXJ0bWVudCBvZiBGYWN1bHR5IG9mIFNjaWVuY2UfRGVwYXJ0bWVudCBvZiBGaW5hbmNpYWwgU3R1ZGllcxZEZXBhcnRtZW50IG9mIEdlbmV0aWNzF0RlcGFydG1lbnQgb2YgR2VvZ3JhcGh5FURlcGFydG1lbnQgb2YgR2VvbG9neSpEZXBhcnRtZW50IG9mIEdlcm1hbmljIGFuZCBSb21hbmNlIFN0dWRpZXMTRGVwYXJ0bWVudCBvZiBIaW5kaRVEZXBhcnRtZW50IG9mIEhpc3RvcnkbRGVwYXJ0bWVudCBvZiBIaXN0b3J5IChTREMpGkRlcGFydG1lbnQgb2YgSG9tZSBTY2llbmNlTkRlcGFydG1lbnQgb2YgSW5kaXJhIEdhbmRoaSBJbnN0aXR1dGUgb2YgUGh5c2ljYWwgRWR1Y2F0aW9uIGFuZCBTcG9ydHMgU2NpZW5jZTVEZXBhcnRtZW50IG9mIEludGVyLURpc2NpcGxpbmFyeSBBbmQgQXBwbGllZCBTY2llbmNlcxJEZXBhcnRtZW50IG9mIExDLUktRGVwYXJ0bWVudCBvZiBMaWJyYXJ5IGFuZCBJbmZvcm1hdGlvbiBTY2llbmNlGURlcGFydG1lbnQgb2YgTGluZ3Vpc3RpY3MZRGVwYXJ0bWVudCBvZiBNYXRoZW1hdGljcxpEZXBhcnRtZW50IG9mIE1pY3JvYmlvbG9neRVEZXBhcnRtZW50IG9mIE1JTCYgTFMTRGVwYXJ0bWVudCBvZiBNdXNpYyJEZXBhcnRtZW50IG9mIE9wZXJhdGlvbmFsIFJlc2VhcmNoFURlcGFydG1lbnQgb2YgUGVyc2lhbhhEZXBhcnRtZW50IG9mIFBoaWxvc29waHkeRGVwYXJ0bWVudCBvZiBQaGlsb3NvcGh5IChTREMpFURlcGFydG1lbnQgb2YgUGh5c2ljcyVEZXBhcnRtZW50IG9mIFBsYW50IE1vbGVjdWxhciBCaW9sb2d5H0RlcGFydG1lbnQgb2YgUG9saXRpY2FsIFNjaWVuY2UYRGVwYXJ0bWVudCBvZiBQc3ljaG9sb2d5FURlcGFydG1lbnQgb2YgUHVuamFiaRZEZXBhcnRtZW50IG9mIFNhbnNrcml0L0RlcGFydG1lbnQgb2YgU2xhdm9uaWMgQW5kIEZpbm5vLVVncmlhbiBTdHVkaWVzHURlcGFydG1lbnQgb2YgU29jaWFsIFNjaWVuY2VzGURlcGFydG1lbnQgb2YgU29jaWFsIFdvcmsXRGVwYXJ0bWVudCBvZiBTb2Npb2xvZ3kYRGVwYXJ0bWVudCBvZiBTdGF0aXN0aWNzEkRlcGFydG1lbnQgb2YgVXJkdRVEZXBhcnRtZW50IG9mIFpvb2xvZ3kYRGVzaGJhbmRodSBDb2xsZWdlIChEYXkpI0RyLiBCLlIuIEFtYmVka2FyIChUZWFjaGluZyBDZW50cmUpMERyLiBCLlIuIEFtYmVka2FyIENlbnRlciBmb3IgQmlvbWVkaWNhbCBSZXNlYXJjaB1Eci4gQmhpbSBSYW8gQW1iZWRrYXIgQ29sbGVnZTVEdXJnYWJhaSBEZXNobXVraCBDb2xsZWdlIG9mIFNwZWNpYWwgRWR1Y2F0aW9uIChWLkkuKRhEeWFsIFNpbmdoIENvbGxlZ2UgKERheSkYRHlhbCBTaW5naCBDb2xsZWdlIChFdmUpHUZhY3VsdHkgb2YgTWFuYWdlbWVudCBTdHVkaWVzDUdhcmdpIENvbGxlZ2UQSGFucyBSYWogQ29sbGVnZSJIYW5zIFJhaiBDb2xsZWdlIC0gVGVhY2hpbmcgQ2VudHJlDUhpbmR1IENvbGxlZ2UVSS5QLkNvbGxlZ2UgRm9yIFdvbWVuNkluZGlyYSBHYW5kaGkgSW5zdGl0dXRlIG9mIFBoeS4gRWR1LiAmIFNwb3J0cyBTY2llbmNlcy5JbnN0aXR1dGUgb2YgQ3liZXIgU2VjdXJpdHkgYW5kIExhdyAoSS5DLlMuTC4pG0luc3RpdHV0ZSBPZiBIb21lIEVjb25vbWljcy5JbnN0aXR1dGUgb2YgSW5mb3JtYXRpY3MgJiBDb21tdW5pY2F0aW9uIChJSUMpG0phbmtpIERldmkgTWVtb3JpYWwgQ29sbGVnZS1KYW5raSBEZXZpIE1lbW9yaWFsIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUUSmVzdXMgJiBNYXJ5IENvbGxlZ2UmSmVzdXMgJiBNYXJ5IENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUMSnViaWxlZSBIYWxsD0thbGluZGkgQ29sbGVnZSFLYWxpbmRpIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUTS2FtbGEgTmVocnUgQ29sbGVnZSRLZXNoYXYgTWFoYXZpZGxheWEgKFRlYWNoaW5nIENlbnRyZSkUS2VzaGF2IE1haGF2aWR5YWxheWESS2lyb3JpIE1hbCBDb2xsZWdlEkxhZHkgSXJ3aW4gQ29sbGVnZR9MYWR5IFNocmkgUmFtIENvbGxlZ2UgZm9yIFdvbWVuEkxha3NobWliYWkgQ29sbGVnZSRMYWtzaG1pYmFpIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUMTEFXIENFTlRSRS1JDUxBVyBDRU5UUkUtSUkYTWFoYXJhamEgQWdyYXNlbiBDb2xsZWdlKk1haGFyYWphIEFncmFzZW4gQ29sbGVnZSAtIFRlYWNoaW5nIENlbnRyZSVNYWhhcnNoaSBWYWxtaWtpIENvbGxlZ2Ugb2YgRWR1Y2F0aW9uEE1haXRyZXlpIENvbGxlZ2UiTWFpdHJleWkgQ29sbGVnZSAtIFRlYWNoaW5nIENlbnRyZR1NYXRhIFN1bmRyaSBDb2xsZWdlIEZvciBXb21lbi9NYXRhIFN1bmRyaSBDb2xsZWdlIEZvciBXb21lbiAtIFRlYWNoaW5nIENlbnRyZQ1NaXJhbmRhIEhvdXNlH01pcmFuZGEgSG91c2UgKFRlYWNoaW5nIENlbnRyZSkcTW90aSBMYWwgTmVocnUgQ29sbGVnZSAoRGF5KRxNb3RpIExhbCBOZWhydSBDb2xsZWdlIChFdmUpKE1vdGkgTGFsIE5laHJ1IENvbGxlZ2UgKFRlYWNoaW5nIENlbnRyZSksTm9uIENvbGxlZ2lhdGUgV29tZW4gRWR1Y2F0aW9uIEJvYXJkIChOQ1dFQikYUC5HLkQuQS5WLiBDb2xsZWdlIChEYXkpGFAuRy5ELkEuVi4gQ29sbGVnZSAoRXZlKSRQLkcuRC5BLlYuIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUQUmFqZGhhbmkgQ29sbGVnZSJSYWpkaGFuaSBDb2xsZWdlIChUZWFjaGluZyBDZW50cmUpG1JhbSBMYWwgQW5hbmQgQ29sbGVnZSAoRGF5KRFSYW1hbnVqYW4gQ29sbGVnZSNSYW1hbnVqYW4gQ29sbGVnZSAoVGVhY2hpbmcgQ2VudHJlKQ5SYW1qYXMgQ29sbGVnZRdTLkcuVC5CLiBLaGFsc2EgQ29sbGVnZRdTYXR5YXdhdGkgQ29sbGVnZSAoRGF5KRdTYXR5YXdhdGkgQ29sbGVnZSAoRXZlKSNTYXR5YXdhdGkgQ29sbGVnZSAoVGVhY2hpbmcgQ2VudHJlKRdTY2hvb2wgb2YgT3BlbiBMZWFybmluZyJTaGFoZWVkIEJoYWdhdCBTaW5naCBDb2xsZWdlIChEYXkpIlNoYWhlZWQgQmhhZ2F0IFNpbmdoIENvbGxlZ2UgKEV2ZSk1U2hhaGVlZCBSYWpndXJ1IENvbGxlZ2Ugb2YgQXBwbGllZCBTY2llbmNlcyBmb3IgV29tZW4rU2hhaGVlZCBTdWtoZGV2IENvbGxlZ2Ugb2YgQnVzaW5lc3MgU3R1ZGllcw9TaGl2YWppIENvbGxlZ2UXU2h5YW0gTGFsIENvbGxlZ2UgKERheSkXU2h5YW0gTGFsIENvbGxlZ2UgKEV2ZSkxU2h5YW1hIFByYXNhZCBNdWtoZXJqZWUgQ29sbGVnZSAtIFRlYWNoaW5nIENlbnRyZShTaHlhbWEgUHJhc2FkIE11a2hlcmppIENvbGxlZ2UgZm9yIFdvbWVuFlNPTCBTdHVkeSBDZW50ZXIgU291dGgbU3JpIEF1cm9iaW5kbyBDb2xsZWdlIChEYXkpG1NyaSBBdXJvYmluZG8gQ29sbGVnZSAoRXZlKSdTcmkgQXVyb2JpbmRvIENvbGxlZ2UgKFRlYWNoaW5nIENlbnRyZSkpU3JpIEd1cnUgR29iaW5kIFNpbmdoIENvbGxlZ2UgT2YgQ29tbWVyY2U7U3JpIEd1cnUgR29iaW5kIFNpbmdoIENvbGxlZ2UgT2YgQ29tbWVyY2UgLSBUZWFjaGluZyBDZW50cmUhU3JpIEd1cnUgTmFuYWsgRGV2IEtoYWxzYSBDb2xsZWdlG1NyaSBSYW0gQ29sbGVnZSBPZiBDb21tZXJjZRhTcmkgVmVua2F0ZXN3YXJhIENvbGxlZ2UUU3QuIFN0ZXBoZW5zIENvbGxlZ2UaU3dhbWkgU2hyYWRkaGFuYW5kIENvbGxlZ2UTVW5pdmVyc2l0eSBvZiBEZWxoaRNWaXZla2FuYW5kYSBDb2xsZWdlJVZpdmVrYW5hbmRhIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUaWmFraXIgSHVzYWluIENvbGxlZ2UgKEV2ZSkgWmFraXIgSHVzYWluIERlbGhpIENvbGxlZ2UgKERheSkVowESPC0tLS0tU2VsZWN0LS0tLS0+AzAwMQMzMzIDMDAyAzMzMwMwNTkDMDAzAzAwNwMzMzUDMDA4AzMyNQMwMDkDMzA5AzMxMgMwMTMDMzM2AzAxNAMwMTUDMzQ0AzAxNgMzMTYDMjI1AzIyNgMyMTUDMjAxAzI5MAMyNTgDMjQ5AzIxNgMyMDIDMjQ4AzIxNwMyNDEDMjM0AzIyOAMyMjcDMjQzAzI1MQMyMDMDMjE4AzEwMQMxMTQDMjU5AzI1MgMyMjkDMjE5AzIwNAMyMDUDMjMxAzI5MQMyMjADMjU1AzEwNwMyMzkDMjA2AzIwNwMyMzUDMjUzAzIwOAMyNDADMjM2AzIwOQMyMTADMzQ5AzIyMgMyNjEDMjMyAzIxMQMyMTIDMjEzAzI0MgMxMTUDMjMzAzIzMAMyMzcDMjE0AzIyMwMwMTkDMzM0AzMxOAMwMTADMzE0AzAyMQMwMjIDMTA5AzAyNAMwMjUDMzMxAzAyNgMwMjkDMDI4AzMxNwMwMzADMjg1AzAzMQMzMjIDMDMyAzMyNgMzMDYDMDMzAzMyMwMwMzQDMzM3AzAzNQMwMzYDMDM4AzAzOQMwNDADMzI4AzMxMAMzMTEDMDQxAzMyMAMzMTUDMDQzAzMyNwMwNDQDMzIxAzA0NwMzMzgDMDQ4AzA0OQMzMzkDMzA3AzA1MwMwNTQDMzI5AzA1NQMzNDADMDU4AzAyMAMzNDEDMDU2AzA2OAMwNjIDMDYzAzM0MgNTT0wDMDY0AzA2NQMwNjYDMDY3AzA3MQMwNzMDMDc0AzMyNAMwNzUEU09MUwMwNzYDMDc3AzM0MwMwNzgDMzMwAzA2OQMwNzIDMDc5AzA4MAMwODEDMTAwAzA4NAMzMTkDMDg2AzA4NRQrA6MBZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAh0PZBYCZg9kFgICAw8PFgIeCEltYWdlVXJsBUNHZW5lcmF0ZUNhcHRjaGEuYXNweD9DYXB0Y2hhQ29kZT0xMTc1MDMmRGF0ZVRpbWU9NjM3Mzg0NjYzNDczMTUzNzE3ZGQCJw8PFgIeB1Zpc2libGVoZGQCLw8PFgIfB2hkZGQUS4QXZyokNAgJQMZZXNntJV0AMA=="""

CONST_VIEWSTATEGENERATOR = """35D4F7A9"""

CONST_EVENTVALIDATION = """/wEWqQECm9mUOALAn+vmDAKrw9qnCgLKlPHFDgLA/IyBCALY65qqAgLl6+6qAgL9gv23BALopo/rCQL+gsG3BALi5fmADwKr17HqAwLXj7neBwKr173qAwLoppvrCQLvppvrCQLY6+KqAgL+gsW3BALMzpP3BQKTuKfBCQK017nqAwKWuNPACQLJzpv3BQLMzpv3BQKq173qAwLPzp/3BQKq17nqAwLG/IyBCAKtxY70BgLVj63eBwLupovrCQLPzpv3BQLb6+6qAgLVj6neBwLg5f2ADwLG/LyBCAKRuN/ACQLVj7HeBwLg5fGADwL8gvG3BALG/LCBCAL8gsG3BALVj73eBwLB/IyBCAKQuKfBCQLupo/rCQLb65KqAgLuppPrCQLupp/rCQKRuKPBCQKq14XqAwLG/LiBCALG/OCBCAKtxaL0BgKq16nqAwLj5fmADwLuppfrCQLPzuf3BQLg5fmADwKq17HqAwL8gvW3BALVj7neBwKtxdr3BgLPzpP3BQLuppvrCQKtxa70BgLvpovrCQLb6+aqAgLG/LSBCALb65qqAgLG/ICBCALb6+KqAgL8gsW3BALb656qAgK117nqAwL8gv23BAKtxab0BgLg5fWADwKRuKfBCQL8gvm3BALopp/rCQKWuN/ACQLKj73eBwKvxa70BgKWuKfBCQLA/ISBCALl6+aqAgLpppvrCQKTuNvACQK0173qAwLH/LiBCALJzp/3BQLoppPrCQLXj7HeBwLh5f2ADwKvxab0BgKq1+XqAwLA/LiBCALY6+aqAgLl65qqAgLMzp/3BQLMzuf3BQL+gv23BAL9gvm3BAKTuN/ACQLh5fWADwK017HqAwLJzpP3BQLXj7XeBwLoppfrCQKvxdr3BgLKj7HeBwKixa70BgLH/ICBCALA/LyBCAKixaL0BgKr17nqAwL+gvG3BALh5fGADwKTuNPACQLH/ISBCALi5emADwLKj7XeBwLXj6neBwLopovrCQLvppfrCQLh5fmADwL+gvW3BAKTuNfACQLvppPrCQK016nqAwKixdr3BgLXj63eBwKvxaL0BgLH/LyBCALJzov3BQLXj6HeBwLl65aqAgL+gum3BALY656qAgKuwq+LCAKTuMvACQK0163qAwLJzo/3BQLi5eGADwLA/KiBCAL+gu23BAKTuM/ACQKWuNvACQK016HqAwKuwqv+CQLJzoP3BQLi5eWADwL9gvG3BALXj6XeBwKixab0BgLopoPrCQLl64qqAgLopofrCQKvxYr0BgLA/OyBCAKsxar0BgKTuIPBCQLvpp/rCQLJzsf3BQK01+XqAwK097DwDALvmdGCAwKln/OLAqnoHgH26DG+FX09379Ly9yBzf/x"""

# store marks list for all DU
college_sgpa_list = []
college_aggregate_sgpa_list = []

# override for one college check
all_colleges = [
    "1724501"
]

for col in all_colleges:
    dduc = []
    constantCollegePart = col[:-2]
    for i in range(1,10):
        dduc.append([constantCollegePart + '0' + str(i)])
    for i in range(10,50):
        dduc.append([constantCollegePart + str(i)])
    
    # testing generation of rollnos
    # print(dduc)
    # break
    # dduc = [['17015570001']]
    VAR_collegeCode = "234"   
    for VAR_stud in dduc:
        VAR_rollno = VAR_stud[0]
        # print(VAR_rollno)
        payload = {
            '__EVENTTARGET' : '',
            '__EVENTARGUMENT' : '',
            '__VIEWSTATE': CONST_VIEWSTATE,
            '__VIEWSTATEGENERATOR': CONST_VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': CONST_EVENTVALIDATION,
            'ddlcollege' : VAR_collegeCode,
            'txtrollno' : VAR_rollno,
            'txtcaptcha' : '117503',
            'btnsearch': 'Print+Score+Card'
            }
        
        # infinite cookie life
        cookies = {'ASP.NET_SessionId': 'efstl5454kxusy45e35h45j1'}

        soup = None
        count = 0
        while(soup == None):
            r = requests.post(GradeCard, data=payload, cookies=cookies)
            # print(r.text)
            # exit
            soup = BeautifulSoup(r.text, 'html.parser')
            if(soup==None):
                continue
            # print(soup.title.string)
            if(soup.title.string == "Runtime Error"):
                if count == 5:
                    break
                else:
                    count = count + 1
                soup = None
                continue
        
        if count == 5:
            continue
        # for img in soup.find_all('img'):
        #     img.decompose()

        #t = soup.find('span', attrs={'id':'lblstatement'}).decompose()
        #t = soup.find('span', attrs={'id':'lbl_sub_head3'}).decompose()
        #t = soup.find('span', attrs={'id':'lbldisclaimer'}).decompose()
        
        # // todo 
        # sgpa_table = soup.find("span", {"id": "lbl_gr_cgpa"})
        # print(soup)
        # print(college_sgpa_list)

        if soup.find("span", id="lblcollege") == None:
            continue
        if soup.find("span", id="lblname") == None:
            continue
        
        VAR_college = soup.find("span", id="lblcollege").text
        VAR_sname = soup.find("span", id="lblname").text

        # writing result to html file
        # savePath = "html/"+VAR_college.replace(' ', '_')
        # if not os.path.isdir(savePath):
            # os.mkdir(savePath)
        # VAR_filename = savePath + '/' + VAR_rollno + '__' + VAR_sname + '__' + '.html'
        # with open(VAR_filename, "w") as file:
            # file.write(str(soup))

        # print(VAR_college, VAR_sname);
        # total = soup.find("table", id="lblgrandtotal")
        sgpa_table = soup.find("table", {"id": "gvrslt"})
        if(sgpa_table == None ):
            continue

        # GET 6th sem marks
        try:
            obtained_marks = int(sgpa_table.findAll('tr')[4].findAll('td')[1].text)
            total_marks = 5
            # see exact marks and not percentage
            FINAL_CGPA = obtained_marks
            print([VAR_rollno, VAR_sname, FINAL_CGPA, VAR_college])

        except IndexError:
            continue

        college_sgpa_list.append([VAR_rollno, VAR_sname, FINAL_CGPA, VAR_college])

        # GET Aggregate marks

        try:
            sems = sgpa_table.findAll('tr')
            obtained_marks = 0
            for i in range(1,len(sems)):
                obtained_marks = obtained_marks + int(sems[i].findAll('td')[1].text)
            total_marks = 5*6 # we have 6 sems
            FINAL_CGPA = (obtained_marks)/total_marks
            print([VAR_rollno, VAR_sname, FINAL_CGPA, VAR_college])

        except IndexError:
            continue
        
        college_aggregate_sgpa_list.append([VAR_rollno, VAR_sname, FINAL_CGPA, VAR_college])

        
college_sgpa_list.sort(key = lambda x : x[2], reverse=True)
college_aggregate_sgpa_list.sort(key = lambda x : x[2], reverse=True)

# print(college_sgpa_list)

# 6TH SEM PRINT

# print to file
with open('DU-PG-MCA-2020-6th-sem.txt','w') as f:
    print('{3:<5} {0:15} {1:25} {2:10} {4:<40}'.format("Roll No.","Name","Sem-VI","S.No", "College"), file=f)
    for i,marks in enumerate(college_sgpa_list):
        print('{3:<5} {0:15} {1:25} {2:<10} {4:<40}'.format(marks[0],marks[1],marks[2], i+1, marks[3]), file=f)

# CSV print to file
with open('DU-PG-MCA-2020-6th-sem.csv.txt','w') as f:
    print('{3:<5} ,{0:15} ,{1:25} ,{2:10} ,{4:<40}'.format("Roll No.","Name","Sem-VI","S.No", "College"), file=f)
    for i,marks in enumerate(college_sgpa_list):
        print('{3:<5} ,{0:15} ,{1:25} ,{2:<10} ,{4:<40}'.format(marks[0],marks[1],marks[2], i+1, marks[3]), file=f)


# AGGREGATE PRINT

# print to file
with open('DU-PG-MCA-2017-2020-aggregate.txt','w') as f:
    print('{3:<5} {0:15} {1:25} {2:10} {4:<40}'.format("Roll No.","Name","aggregate","S.No", "College"), file=f)
    for i,marks in enumerate(college_aggregate_sgpa_list):
        print('{3:<5} {0:15} {1:25} {2:<10} {4:<40}'.format(marks[0],marks[1],marks[2], i+1, marks[3]), file=f)

# CSV print to file
with open('DU-PG-MCA-2017-2020-aggregate.csv.txt','w') as f:
    print('{3:<5} ,{0:15} ,{1:25} ,{2:10} ,{4:<40}'.format("Roll No.","Name","aggregate","S.No", "College"), file=f)
    for i,marks in enumerate(college_aggregate_sgpa_list):
        print('{3:<5} ,{0:15} ,{1:25} ,{2:<10} ,{4:<40}'.format(marks[0],marks[1],marks[2], i+1, marks[3]), file=f)

# print(soup.prettify())

# with open("test.html", "w") as file:
#     file.write(str(soup))
