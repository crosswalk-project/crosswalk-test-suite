/*
Copyright (c) 2015 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:
        Xu, Kang <kangx.xu@intel.com>

*/

var privateKey = null;
var publicKey = null;
var signatureKey = null

function generateKeyPair() {
	crypto.subtle.generateKey(
	    { name: "RSASSA-PKCS1-v1_5", modulusLength: 2048, publicExponent: new Uint8Array([0x01, 0x00, 0x01]), hash: {name: "SHA-256"}},
		false,
		["sign", "verify"]
    )
    .then(function(key){
        privateKey = key.privateKey;
        publicKey = key.publicKey;
        $('#publicKey').text("public key:" + key.publicKey + "\nprivate key:" + key.privateKey);
    })
    .catch(function(err){
        $('#publicKey').text("Generate key pair failed");
    });
};

function signData() {
    
    if ( privateKey ){
	    crypto.subtle.sign(
            {
                name: "RSASSA-PKCS1-v1_5"
            },
            privateKey,
            new Uint8Array([0x01, 0x00, 0x01])
        )
        .then(function(signature){
            signatureKey = signature;
            $('#publicKey').text("signature data:" + signature);
        })
        .catch(function(err){
            $('#publicKey').text("Sign data failed");
        });
    } else {
        $('#publicKey').text("No private key can be used, pls generate key");
    }
}

function verifyData() {

    if ( signatureKey ){
	    crypto.subtle.verify(
            {
                name: "RSASSA-PKCS1-v1_5"
            },
            publicKey,
            signatureKey,
            new Uint8Array([0x01, 0x00, 0x01])
        )
        .then(function(isvalid){
            $('#publicKey').text("verify data:" + isvalid);
        })
        .catch(function(err){
            $('#publicKey').text("verify data failed");
        });
    } else {
        $('#publicKey').text("No signature can be used, pls generate key and sign");
    }
}
